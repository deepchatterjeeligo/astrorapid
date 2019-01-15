import os
import numpy as np
import h5py
import multiprocessing as mp
import pandas as pd
import argparse

from astrorapid.read_from_database.get_data import GetData
from astrorapid.process_light_curves import InputLightCurve


def read_light_curves_from_sql_database(data_release, fname, field_in='%', model_in='%', batch_size=100, offset=0, sort=True, redo=False, passbands=('g', 'r'), known_redshift=True):
    print(fname)

    extrasql = ''  # "AND (objid LIKE '%00' OR objid LIKE '%50' OR sim_type_index IN (51,61,62,63,64,84,90,91,93))"  # ''#AND sim_redshift_host < 0.5 AND sim_peakmag_r < 23'
    getter = GetData(data_release)
    result = getter.get_lcs_data(columns=['objid', 'ptrobs_min', 'ptrobs_max', 'sim_peakmag_r', 'sim_redshift_host', 'mwebv', 'sim_dlmu', 'peakmjd', 'mwebv', 'ra', 'decl', 'hostgal_photoz', 'hostgal_photoz_err'],
                                 field=field_in, model=model_in, snid='%', limit=batch_size, offset=offset, shuffle=False, sort=sort, extrasql=extrasql)

    store = pd.HDFStore(fname)

    for head, phot in result:
        objid, ptrobs_min, ptrobs_max, peakmag, redshift, mwebv, dlmu, peakmjd, mwebv, ra, dec, photoz, photozerr = head

        field, model, base, snid = objid.split('_')

        lc = getter.convert_pandas_lc_to_recarray_lc(phot, passbands=passbands)

        inputlightcurve = InputLightCurve(lc['mjd'], lc['flux'], lc['fluxerr'], lc['pb'], lc['zpt'], lc['photflag'], ra,
                                          dec, objid, redshift, mwebv, known_redshift=known_redshift,
                                          training_set_parameters={'class_number': int(model), 'peakmjd': peakmjd})

        savepd = inputlightcurve.preprocess_light_curve()
        store.append(objid, savepd)

    store.close()
    print("saved %s" % fname)


def combine_hdf_files(save_dir, combined_savename):
    fnames = os.listdir(save_dir)
    fname_out = os.path.join(ROOT_DIR, 'earlyclass', combined_savename)
    output_file = h5py.File(fname_out, 'w')


    for n, f in enumerate(fnames):
        print(n, f)
        try:
            f_hdf = h5py.File(os.path.join(save_dir, f), 'r')
            for objid in f_hdf.keys():
                objid = objid.encode('utf-8')
                h5py.h5o.copy(f_hdf.id, objid, output_file.id, objid)
            f_hdf.close()
        except OSError as e:
            print("Failed to open file", "f")
            print(e)
    output_file.close()


def create_all_hdf_files(args):
    data_release, i, save_dir, field_in, model_in, batch_size, sort, redo, passbands = args
    offset = batch_size * i
    fname = os.path.join(save_dir, 'earlylc_{}.hdf5'.format(i))
    read_light_curves_from_sql_database(data_release=data_release, fname=fname, field_in=field_in, model_in=model_in,
                           batch_size=batch_size, offset=offset, sort=sort, redo=redo, passbands=passbands)


def main():
    multiprocessing = False
    passbands = ('g', 'r')
    data_release = 'ZTF_20180716'
    field = 'MSIP'
    model = '%'

    # Get number of objects
    # extrasql = ''
    # getter = GetData(data_release)
    # nobjects = next(getter.get_lcs_headers(field=field, model=model, get_num_lightcurves=True, big=False, extrasql=extrasql))
    # print("{} objects for model {} in field {}".format(nobjects, model, field))

    batch_size = 1000
    sort = True
    redo = True

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', "--offset", type=int)
    parser.add_argument('-n', "--offsetnext", type=int)
    args = parser.parse_args()
    if args.offset is not None:
        offset = args.offset
    else:
        offset = 0
    if args.offsetnext is not None:
        offset_next = args.offsetnext
    else:
        offset_next = 2200
    print(offset, offset_next)

    training_set_dir = 'training_set_files'
    save_dir = os.path.join(training_set_dir, 'saved_lc_{}_{}'.format(field, data_release))
    if not os.path.exists(save_dir) and offset == 0:
        os.makedirs(save_dir)

    # Multiprocessing
    i_list = np.arange(offset, offset_next)
    print(i_list)
    args_list = []
    file_list = os.listdir(save_dir)
    for i in i_list:
        if 'earlylc_{}.hdf5'.format(i) not in file_list:
            print(os.path.join(save_dir, 'earlylc_{}.hdf5'.format(i)))
            args_list.append((data_release, i, save_dir, field, model, batch_size, sort, redo, passbands))

    if multiprocessing:
        pool = mp.Pool(processes=1)
        results = pool.map_async(create_all_hdf_files, args_list)
        pool.close()
        pool.join()
    else:
        for args in args_list:
            create_all_hdf_files(args)

    combine_hdf_files(save_dir, 'saved_lc_{}_{}.hdf5'.format(field, data_release))


if __name__ == '__main__':
    main()

