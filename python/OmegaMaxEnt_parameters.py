
# parameters set exclusively by the function compute_scalar_GfReFreq()
data_str = "data file:"
err_str = "error file:"
boson_str = "bosonic data (yes/[no]):"
time_str = "imaginary time data (yes/[no]):"
# temp_str = "temperature (in energy units, k_B=1):"

# optional parameters
OmegaMaxEnt_input_params = dict(
# OPTIONAL PREPROCESSING TIME PARAMETERS
# DATA PARAMETERS
    G_inf_finite="finite value at infinite frequency (yes/[no]):",
    G_inf="value at infinite frequency:",
    norm="norm of spectral function:",
    M1="1st moment:",
    errM1="1st moment error:",
    M2="2nd moment:",
    errM2="2nd moment error:",
    M3="3rd moment:",
    errM3="3rd moment error:",
    omega_n_trunc="truncation frequency:",
# INPUT FILES PARAMETERS
    input_dir="input directory:",
    col_Gi="Im(G) column in data file (default: 3):",
    error_file="error file:",
    cov_re_re="re-re covariance file:",
    cov_im_im="im-im covariance file:",
    cov_re_im="re-im covariance file:",
    cov_tau="imaginary time covariance file:",
    added_noise="added noise relative error (s1 s2 ...) (default: 0):",
# FREQUENCY GRID PARAMETERS
    cutoff_omega_n="Matsubara frequency cutoff (in energy units, k_B=1):",
    spectrum_width="spectral function width:",
    spectrum_center="spectral function center:",
    freq_grid_origin="real frequency grid origin:",
    freq_step="real frequency step:",
    freq_grid="real frequency grid file:",
    non_uniform_grid="use non uniform grid in main spectral range (yes/[no]):",
    use_parameterized_grid="use parameterized real frequency grid (yes/[no]):",
    parameterized_grid_params="grid parameters (w_0 dw_0 w_1 dw_1 ... w_{N-1} dw_{N-1} w_N):",
    output_grid_params="output real frequency grid parameters (w_min dw w_max):",
# COMPUTATION OPTIONS
    eval_moments="evaluate moments (yes/[no]):",
    maximum_moment="maximum moment:",
    def_model_center="default model center (default: 1st moment):",
    def_model_width="default model half width (default: standard deviation):",
    def_model_shape_param="default model shape parameter (default: 2):",
    def_model_file="default model file:",
    initial_spectrum="initial spectral function file:",
    compute_Pade="compute Pade result (yes/[no]):",
    n_freq_Pade="number of frequencies for Pade:",
    eta_Pade="imaginary part of frequency in Pade:",
# PREPROCESSING EXECUTION OPTIONS
    preprocess_only="preprocess only (yes/[no]):",
    displ_preproc_figs="display preprocessing figures (yes/[no]):",
    displ_adv_preproc_figs="display advanced preprocessing figures (yes/[no]):",
    print_other_params="print other parameters (yes/[no]):",
# OPTIONAL MINIMIZATION TIME PARAMETERS
# OUTPUT FILES PARAMETERS
    output_dir="output directory:",
    output_fname_suffix="output file names suffix:",
    alpha_max_saved="maximum alpha for which results are saved:",
    alpha_min_saved="minimum alpha for which results are saved:",
    spectrum_sample_freq="spectral function sample frequencies (w_1 w_2 ... w_N):",
# COMPUTATION PARAMETERS
    alpha_init="initial value of alpha:",
    alpha_min="minimum value of alpha:",
    alpha_opt_max="maximum optimal alpha:",
    alpha_opt_min="minimum optimal alpha:",
# MINIMIZATION EXECUTION OPTIONS
    n_alpha_values="number of values of alpha computed in one execution:",
    init_maxent="initialize maxent (yes/[no]):",
    init_preproc="initialize preprocessing (yes/[no]):",
    interactive_mode="interactive mode ([yes]/no):",
# DISPLAY OPTIONS
    print_result="print results at each value of alpha (yes/[no]):",
    displ_alpha_opt_figs="show optimal alpha figures ([yes]/no):",
    displ_alpha_min_figs="show lowest alpha figures ([yes]/no):",
    displ_alpha_curves="show alpha dependant curves ([yes]/no):",
    ref_spectrum="reference spectral function file:")


# internal parameters (advanced)
OmegaMaxEnt_other_params = dict(
    Nn_min="Nn_min, minimum number of Matsubara frequencies:",
    Nn_max="Nn_max, maximum number of Matsubara frequencies:",
    Nw_min="Nw_min, minimum number of real frequencies:",
    Nw_max="Nw_max, maximum number of real frequencies:",
    Nn_fit_max="Nn_fit_max, initial maximum number of frequencies used to fit the asymptotic form during computation of moments:",
    Nn_fit_fin="Nn_fit_fin, final maximum number of frequencies used to fit the asymptotic form during computation of moments:",
    Nn_as_min="Nn_as_min, minimum number of frequencies in the asymptotic region:",
    Niter_dA_max="Niter_dA_max, maximum number of iterations in Newton's method for a given value of alpha:",
    Nwsamp="Nwsamp, default number of sample frequencies of spectral function to be save as a function of alpha:",
    Nsmooth_errG="Nsmooth_errG, smoothing distance for the added noise error:",
    f_SW_std_omega="f_SW_std_omega, ratio of main spectral range and standard deviation of spectrum:",
    f_w_range="f_w_range, total real frequency range=f_w_range*(spectral function width):",
    Rmin_SW_dw="Rmin_SW_dw, minimum ratio of standard deviation and frequency step:",
    tol_tem="tol_tem, relative tolerance between temperature extracted from Matsubara frequency and input temperature:",
    tol_Ginf="tol_Ginf, tolerance on frequency-independent part of data:",
    tol_norm="tol_norm, tolerance on norm extracted from high frequency:",
    tol_M1="tol_M1, tolerance between 1st moment extracted from high frequency and input one:",
    tol_M2="tol_M2, tolerance between 2nd moment extracted from high frequency and input one:",
    tol_M3="tol_M3, tolerance between 3rd moment extracted from high frequency and input one:",
    default_error_G="default_error_G, default error on the input data:",
    err_norm="err_norm, relative error on norm:",
    default_error_M="default_error_M, default error on moments:",
    tol_mean_C1="tol_mean_C1, tolerance on mean(M0(n)):",
    tol_std_C1="tol_std_C1, tolerance on std(M0(n)):",
    tol_rdw="tol_rdw, tolerance on ratio of consecutive frequency step:",
    Rmin_Dw_dw="Rmin_Dw_dw, minimum number of steps in a grid interval:",
    Rdw_max="Rdw_max, maximum ratio of steps in consecutive grid interval:",
    RW_grid="RW_grid, grid interval vs transition region ratio:",
    RWD_grid="RWD_grid, transition region vs width parameter ratio:",
    minDefM="minDefM, minimum value of default model:",
    f_alpha_init="f_alpha_init, initial ratio of entropy and chi2 contributions to the spectrum:",
    R_width_ASmin="R_width_ASmin, width of the minimum entropy spectrum relative to spectral function width:",
    f_Smin="f_Smin, minimum entropy term versus optimal chi2 ratio:",
    R_chi2_min="R_chi2_min, minimum ratio of chi2 for consecutive values of alpha:",
    tol_int_dA="tol_int_dA, tolerance on consecutive values of the integral of |dA| in Newton's method:",
    rc2H="rc2H, maximum ratio of the penalization parameter and the maximum eigenvalue of the hessian of chi2:",
    pow_alpha_step_init="pow_alpha_step_init, initial value of the step in log_10(alpha):",
    pow_alpha_step_min="pow_alpha_step_min, minimum value of the step in log_10(alpha):",
    chi2_alpha_smooth_range="chi2_alpha_smooth_range, chi2 vs alpha smoothing range in log10 scale:",
    gamma="f_scale_lalpha_lchi2, log(alpha) scale factor with respect to log(chi2) in the curvature calculation:",
    FNfitTauW="FNfitTauW, factor to determine the number of values of tau in the polynomial fit:",
    std_norm_peak_max="std_norm_peak_max, relative tolerance for standard deviation of low frequency peak weight:",
    varM2_peak_max="varM2_peak_max, relative tolerance on low frequency peak variance:",
    peak_weight_min="peak_weight_min, minimum value of peak weight to assume a low energy peak is present:",
    RMAX_dlchi2_lalpha="RMAX_dlchi2_lalpha, maximum ratio of dlog(chi2)/dlog(alpha) at the lowest alpha and the maximum value:",
    f_alpha_min="f_alpha_min, factor by which alpha_min is reduced when found to be too high:",
    save_alpha_range="save_alpha_range, range of alpha to be saved around the optimal alpha in log10 scale:",
    R_peak_width_dw="R_peak_width_dw, ratio of low energy peak width and low frequency step:",
    R_wncutoff_wr="R_wncutoff_wr, ratio of onset Matsubara frequency of asymptotic region and main spectral range maximum frequency:",
    R_Dw_dw="R_Dw_dw, ratio of grid interval length and step:",
    R_SW_wr="R_SW_wr, ratio of main spectral range maximum frequency and spectrum standard deviation:",
    R_wmax_wr_min="R_wmax_wr_min, minimum ratio of grid maximum frequency and main spectral range maximum frequency:",
    wgt_min_sm="wgt_min_sm, smallest relative weight in the smoothing of the added noise error:",
    R_SW_G_Re_w_range="R_SW_G_Re_w_range, ratio of total frequency range and main spectral region for the real part of G:",
    R_dw_min_dw_dense="R_dw_min_dw_dense, default ratio of the minimal step in the computation grid and the step in the output grid:",
    R_wKK_SW="R_wKK_SW, frequency region around zero where Re[G] is computed with Kramers-Kronig, divided by the spectral function width:",
    R_sv_min="R_sv_min, minimum ratio of matrix singular values in the moments computation in tau:")

Other_params_default_values = dict(
    Nn_min=20,
    Nn_max=500,
    Nw_min=50,
    Nw_max=800,
    Nn_fit_max=200,
    Nn_fit_fin=300,
    Nn_as_min=10,
    Niter_dA_max=20,
    Nwsamp=11,
    Nsmooth_errG=0,
    f_SW_std_omega=3,
    f_w_range=20.0,
    Rmin_SW_dw=50,
    tol_tem=1.0e-8,
    tol_Ginf=1.0e-3,
    tol_norm=0.1,
    tol_M1=0.05,
    tol_M2=0.05,
    tol_M3=0.1,
    default_error_G=1.0e-4,
    err_norm=1.0e-4,
    default_error_M=1e-3,
    tol_mean_C1=0.002,
    tol_std_C1=0.002,
    tol_rdw=1.0e-10,
    Rmin_Dw_dw=4.0,
    Rdw_max=5.0,
    RW_grid=3.0,
    RWD_grid=10.0,
    minDefM=1.0e-20,
    f_alpha_init=1.0e3,
    R_width_ASmin=0.05,
    f_Smin=1.0,
    R_chi2_min=0.8,
    tol_int_dA=1.0e-12,
    rc2H=1.0e12,
    pow_alpha_step_init=0.2,
    pow_alpha_step_min=0.001,
    chi2_alpha_smooth_range=0.5,
    gamma=0.2,
    FNfitTauW=4.0,
    std_norm_peak_max=0.02,
    varM2_peak_max=0.02,
    peak_weight_min=1.0e-4,
    RMAX_dlchi2_lalpha=0.01,
    f_alpha_min=100,
    save_alpha_range=0,
    R_peak_width_dw=10,
    R_wncutoff_wr=10,
    R_Dw_dw=30,
    R_SW_wr=1,
    R_wmax_wr_min=3,
    wgt_min_sm=0.2,
    R_SW_G_Re_w_range=10,
    R_dw_min_dw_dense=5,
    R_wKK_SW=0.01,
    R_sv_min=1e-10)
