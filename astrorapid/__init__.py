from astrorapid.classify import Classify


def main():

    mjd = [57433.4816, 57436.4815, 57439.4817, 57451.4604, 57454.4397, 57459.3963, 57462.418 , 57465.4385, 57468.3768, 57473.3606, 57487.3364, 57490.3341, 57493.3154, 57496.3352, 57505.3144, 57513.2542, 57532.2717, 57536.2531, 57543.2545, 57546.2703, 57551.2115, 57555.2669, 57558.2769, 57561.1899, 57573.2133,57433.5019, 57436.4609, 57439.4587, 57444.4357, 57459.4189, 57468.3142, 57476.355 , 57479.3568, 57487.3586, 57490.3562, 57493.3352, 57496.2949, 57505.3557, 57509.2932, 57513.2934, 57518.2735, 57521.2739, 57536.2321, 57539.2115, 57543.2301, 57551.1701, 57555.2107, 57558.191 , 57573.1923, 57576.1749, 57586.1854]
    flux = [2.0357230e+00, -2.0382695e+00,  1.0084588e+02,  5.5482742e+01,  1.4867026e+01, -6.5136810e+01,  1.6740545e+01, -5.7269131e+01,  1.0649184e+02,  1.5505235e+02,  3.2445984e+02,  2.8735449e+02,  2.0898877e+02,  2.8958893e+02,  1.9793906e+02, -1.3370536e+01, -3.9001358e+01,  7.4040916e+01, -1.7343750e+00,  2.7844931e+01,  6.0861992e+01,  4.2057487e+01,  7.1565346e+01, -2.6085690e-01, -6.8435440e+01, 17.573107  ,   41.445435  , -110.72664   ,  111.328964  ,  -63.48336   ,  352.44907   ,  199.59058   ,  429.83075   ,  338.5255    ,  409.94604   ,  389.71262   ,  195.63905   ,  267.13318   ,  123.92461   ,  200.3431    ,  106.994514  ,  142.96387   ,   56.491238  ,   55.17521   ,   97.556946  ,  -29.263103  ,  142.57687   ,  -20.85057   ,   -0.67210346,   63.353024  ,  -40.02601]
    fluxerr = [42.784702,  43.83665 ,  99.98704 ,  45.26248 ,  43.040398,  44.00679 ,  41.856007,  49.354336, 105.86439 , 114.0044  ,  45.697918,  44.15781 ,  60.574158,  93.08788 ,  66.04482 ,  44.26264 ,  91.525085,  42.768955,  43.228336,  44.178196,  62.15593 , 109.270035, 174.49638 ,  72.6023  ,  48.021034, 44.86118 ,  48.659588, 100.97703 , 148.94061 ,  44.98218 , 139.11194 ,  71.4585  ,  47.766987,  45.77923 ,  45.610615,  60.50458 , 105.11658 ,  71.41217 ,  43.945534,  45.154167,  43.84058 ,  52.93122 ,  44.722775,  44.250145,  43.95989 ,  68.101326, 127.122025, 124.1893  ,  49.952255,  54.50728 , 114.91599]
    passband = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g','r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
    zeropoint = [27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5]
    photflag = [0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 4096, 4096,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0,    0, 4096, 6144, 4096, 4096, 4096, 0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0]
    objid = 'MSIP_01_NONIa-0001_10400862'
    ra = 3.75464531293933
    dec = 0.205076187109334
    redshift = 0.233557
    mwebv = 0.0228761

    light_curve_list = [(mjd, flux, fluxerr, passband, zeropoint, photflag, ra, dec, objid, redshift, mwebv)]

    classification = Classify(light_curve_list)
    predictions = classification.get_predictions()
    print(predictions)

    classification.plot_light_curves_and_classifications()
    classification.plot_classification_animation()


if __name__ == '__main__':
    main()


# Transient Example 1
# mjd = [57434.1263, 57438.1274, 57604.484, 57607.5, 57610.4778, 57613.4821, 57616.4438, 57622.5025, 57630.4831, 57633.4823, 57636.4334, 57639.4221, 57643.4222, 57647.3836, 57650.3981, 57653.4598, 57656.4392, 57659.4389, 57662.3765, 57671.377, 57681.3549, 57687.3573, 57690.3164, 57693.3488, 57697.3358, 57703.3143, 57434.1061, 57607.5015, 57610.4818, 57613.5032, 57616.5022, 57619.46, 57622.4406, 57630.5018, 57633.4595, 57636.4594, 57639.4591, 57647.3977, 57650.4182, 57653.4394, 57656.3982, 57659.3978, 57662.3979, 57668.376, 57671.3563, 57681.3793, 57684.3351, 57697.315, 57703.2954]
# flux = [-51.011257, -198.51755, 514.00244, 357.88925, 309.75653, 317.44543, 106.46677, 134.76555, 184.90858, 131.72256, 151.96513, 174.79182, 46.377613, 411.70862, 80.93826, 166.99916, 91.052475, 171.08084, 133.02815, 82.21088, -17.951181, 51.710495, -52.455284, 13.590807, 102.28364, -172.12567, 25.403301, 1035.0343, 1046.2195, 932.7043, 922.79504, 430.59225, 392.58826, 535.36664, 280.2439, 356.614, 202.10764, 144.86, 617.375, 220.81885, 248.56415, 176.89299, 172.36746, 109.1106, -2.0917137, 74.47287, 130.08217, 127.50506, 230.36594]
# fluxerr = [111.16261, 154.20323, 87.71367, 82.09955, 84.74232, 73.94412, 128.65031, 133.24622, 66.53656, 63.030262, 72.14814, 69.82558, 66.426956, 208.964, 142.56679, 98.74929, 70.88141, 64.46998, 64.96108, 62.825405, 109.5656, 65.04108, 65.725525, 64.73869, 65.50431, 123.69092, 138.49092, 246.11415, 100.33019, 207.86952, 176.95528, 200.56433, 182.27306, 89.147484, 73.51864, 78.44647, 77.51033, 225.18872, 200.55585, 126.7427, 79.653786, 73.403336, 79.01081, 75.72277, 77.96182, 132.20348, 84.35275, 76.10253, 150.20288]
# passband = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
# zeropoint = [27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5]
# photflag = [0, 0, 4096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6144, 0, 4096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# objid = 'MSIP_01_NONIa-0001_1009531'
# ra = 0.893619223529534
# dec = -0.297578637465033
# redshift = 0.0930855
# mwebv = 0.0285932

# Transient Example 2
# mjd = [57433.3649, 57436.3266, 57439.258 , 57443.2409, 57451.2598, 57454.2821, 57459.2594, 57462.2661, 57465.2703, 57468.2596, 57472.1773, 57475.2199, 57478.2213, 57481.2198, 57484.2257, 57487.2001, 57490.1797, 57493.1975, 57496.1958, 57507.2017, 57510.1767, 57513.1797, 57519.2554, 57536.178 , 57539.1992, 57542.2001, 57545.1921, 57551.2035, 57555.2043, 57558.1793, 57651.4884, 57654.5139, 57657.4923, 57660.5122, 57663.5116, 57668.5077, 57671.5109, 57681.5142, 57684.5095, 57687.513 , 57690.5147, 57693.5115, 57697.5089, 57700.4914, 57703.5358, 57433.3229, 57436.2613, 57439.3061, 57443.3372, 57451.2892, 57454.3296, 57459.2411, 57462.2917, 57465.2402, 57468.2388, 57472.2626, 57475.2432, 57478.2399, 57481.206 , 57484.2356, 57487.2215, 57490.2039, 57493.2158, 57496.2216, 57507.1807, 57513.1955, 57528.2011, 57542.1754, 57545.1759, 57551.1849, 57555.2235, 57558.2058, 57648.5074, 57651.511 , 57654.4921, 57657.5114, 57660.5255, 57663.5305, 57668.531 , 57671.5303, 57681.5337, 57684.5349, 57687.5335, 57690.535 , 57693.5324, 57697.4878, 57700.5118, 57703.5541]
# flux = [230.43414  ,  184.88455  ,  172.6806   ,  249.1492   , 99.088776 ,   53.3299   ,   40.45717  ,  -72.15812  , 38.355324 ,  -10.724734 ,   64.60952  ,   81.93845  , -1.9535532,   40.643253 ,  -45.63041  ,   96.80284  ,.503166 ,  -32.878952 ,   11.295108 ,  -36.196854 , 26.743809 ,   -4.249243 ,  -41.312126 ,  -36.279644 ,-15.538207 ,  -77.88097  ,   -5.6148252,   19.292408 , 34.581856 ,  390.6477   , -150.88332  ,  125.234604 ,-26.828035 ,  -61.311554 ,   25.974724 ,   52.979652 , 26.0077   , -118.47624  ,  -31.207022 ,  115.48699  ,-22.280218 ,  -59.73867  ,   54.329372 ,   -0.7030974,-18.00924  ,  233.35193  ,  207.18501  ,  433.4595   ,  205.50656  ,229.06177  ,  192.41536  ,  151.25124  ,   73.2132   ,148.44206  ,   78.0906   ,  153.61783  ,   17.289345 , 19.707968 ,   10.595056 ,   76.158585 ,   58.038044 , 21.523788 ,   47.080894 ,  -65.77096  ,   28.735397 ,-33.11095  ,  227.92462  ,  -48.360638 ,   -9.648249 , 20.067715 , -284.97968  ,  222.4647   , -398.15353  ,248.36769  ,  -92.05493  ,  112.45352  ,  -32.911236 ,  3.576232 ,  -20.299206 ,   59.29004  ,  -27.798334 ,-40.162605 ,    5.0386777,  -61.365643 ,    3.9126327,102.5679   ,  -14.762234 ,   15.1950445]
# fluxerr = [46.052082,  79.89564 , 123.775635,  90.00571 ,  42.881332,  43.517895,  42.310474,  57.44475 ,  82.077095, 107.48741 ,  76.80821 ,  43.840755,  42.27809 ,  43.15124 ,  42.573135,  43.75456 ,  54.4786  ,  71.52536 ,  92.33402 ,  43.28106 ,  43.00488 ,  43.46485 ,  61.894867,  51.614704,  54.53649 ,  59.029667,  62.214954,  82.210526, 107.21878 , 182.42268 , 127.64283 ,  97.46452 ,  80.2688  ,  66.83445 ,  63.74474 ,  59.237015,  58.424442,  96.307594,  78.12063 ,  61.311474,  49.24251 ,  48.431168,  48.661167,  49.09819 ,  45.77172 ,53.89892 ,  84.78499 , 134.79163 , 104.41253 ,  46.486774,  51.07505 ,  43.506985,  58.449215,  86.39472 , 118.43676 , 105.82596 ,  44.402557,  44.93844 ,  47.176216,  46.175434,  43.581013,  55.58769 ,  77.83735 , 100.55842 ,  46.53285 ,  48.585484, 106.447174,  61.866623,  68.44679 ,  93.00254 , 144.07582 , 164.45963 , 221.70703 , 156.10889 , 128.36519 , 101.666275, 121.3949  , 104.361694,  79.50399 ,  73.46456 ,  93.40572 ,  74.18828 ,  64.839714,  52.122   ,  49.58544 ,  55.47642 ,  51.81202 ,  69.04471]
# passband = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
# zeropoint = [27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5]
# photflag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4096,    0,    0,    0, 6144,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0,    0,    0]
# objid = 'MSIP_01_NONIa-0001_10225663'
# ra = 2.57612290563737
# dec = 0.959058423970884
# redshift = 0.358357
# mwebv = 0.0202776