# 根据题号求解，返回list类型,list里的元素是str, result = ['6','1','2']
# questionId是一个字符串"666"，red_word是list:[1,2]
from amyimport import *
from subprocess import call

def doit(questionId, red_word):
    if questionId == "3806282" and len(red_word) == 2:
        return p8_5_ea2_b(red_word)

    elif questionId == "713960" and len(red_word) == 3:
        return p6_1_s_x2(red_word)
    elif questionId == "708925" and len(red_word) == 2:
        return p6_1_t_x3(red_word)
    elif questionId == "1290106" and len(red_word) == 5:
        return p6_1_t_sin_plot(red_word)
    elif questionId == "708927" and len(red_word) == 3:
        return p6_1_t_x2kh(red_word)
    elif questionId == "708935" and len(red_word) == 2:
        return p6_1_t_x2x2(red_word)
    elif questionId == "708984" and len(red_word) == 3:
        return p6_1_t_x2x(red_word)
    elif questionId == "1291008" and len(red_word) == 3:
        return p6_1_cos__cos(red_word)
    elif questionId == "1290504" and len(red_word) == 13:
        return p6_1_gR_L(red_word)
    elif questionId == "1817282" and len(red_word) == 8:
        return p6_1_midpoint(red_word)
    elif questionId == "1816575" and len(red_word) == 3:
        return p6_1_tangent(red_word)
    elif questionId == "1817286" and len(red_word) == 4:
        return p6_1_people(red_word)
    elif questionId == "1387325" and len(red_word) == 2:
        return p6_1_a_b(red_word)
    elif questionId == "1816130" and len(red_word) == 2:
        return p6_1_divides_b(red_word)
    elif questionId == "1817540" and len(red_word) == 13:
        return p6_1_wing_midpoint(red_word)
    elif questionId == "708972" and len(red_word) == 6:
        return p6_1_point_tri(red_word)
    elif questionId == "1291109" and len(red_word) == 3:
        return p6_1_t_area_2(red_word)
    elif questionId == "713971" and len(red_word) == 1:
        return p6_1_s_area_2(red_word)
    elif questionId == "806527" and len(red_word) == 6:
        return p6_1_point_tri(red_word)
    elif questionId == "709741" and len(red_word) == 3:
        return p6_1_t_sqrt(red_word)
    elif questionId == "708936" and len(red_word) == 4:
        return p6_1_t_cos_sin(red_word)
    elif questionId == "708951" and len(red_word) == 3:
        return p6_1_t_2(red_word)
    elif questionId == "709006" and len(red_word) == 2:
        return p6_1_t_2d(red_word)

    elif questionId == "1816097" and len(red_word) == 2:
        return p6_2_figureR3_OA(red_word)
    elif questionId == "1291307" and len(red_word) == 4:
        return p6_2_t_fan_2(red_word)
    elif questionId == "1817544" and len(red_word) == 2:
        return p6_2_figureR1_OC(red_word)
    elif questionId == "1817110" and len(red_word) == 9:
        return p6_2_midpoint(red_word)
    elif questionId == "1817393" and len(red_word) == 2:
        return p6_2_figureR1_OA(red_word)
    elif questionId == "1816521" and len(red_word) == 2:
        return p6_2_figureR2_AB(red_word)
    elif questionId == "4101020" and len(red_word) == 2:
        return p6_2_figureR1_AB(red_word)
    elif questionId == "1816477" and len(red_word) == 2:
        return p6_2_figureR3_AB(red_word)
    elif questionId == "1816073" and len(red_word) == 3:
        return p6_2_tetrahedron(red_word)
    elif questionId == "1291801" and len(red_word) == 2:
        return p6_2_selectab(red_word)
    elif questionId == "1291778" and len(red_word) == 1:
        return p6_2_volume_rotate_x_4sqrt(red_word)
    elif questionId == "1291713" and len(red_word) == 2:
        return p6_2_pyramid_h_a(red_word)
    elif questionId == "1817428" and len(red_word) == 2:
        return p6_2_squares_yare(red_word)
    elif questionId == "1816038" and len(red_word) == 23:
        return p6_2_midpoint_min(red_word)
    elif questionId == "1291178" and len(red_word) == 5:
        return p6_2_x_t_d(red_word)        
    elif questionId == "1386756" and len(red_word) == 3:
        return p6_2_x_t_2d(red_word)   

    elif questionId == "2694103" and len(red_word) == 2:
        return p6_3_a_bx(red_word)
    elif questionId == "2694102" and len(red_word) == 2:
        return p6_3_a_bsin(red_word)
    elif questionId == "1816112" and len(red_word) == 2:
        return p6_3_cylindrical_h_r(red_word)
    elif questionId == "3875268" and len(red_word) == 2:
        return p6_2_volume_rotate_x2(red_word)
    elif questionId == "1817437" and len(red_word) == 2:
        return p6_3_volume_midpoint_f(red_word)
    elif questionId == "1291316" and len(red_word) == 1:
        return p6_3_volume_rotate_y_222(red_word)
    elif questionId == "1817151" and len(red_word) == 3:
        return p6_3_volume_rotate_y_x2(red_word)
    elif questionId == "1576461" and len(red_word) == 4:
        return p6_3_int3(red_word)
    elif questionId == "1387823" and len(red_word) == 4:
        return p6_3_v_t_e2(red_word)
    elif questionId == "1783991" and len(red_word) == 4:
        return p6_3_v_t_sqrt(red_word)
    elif questionId == "1576469" and len(red_word) == 3:
        return p6_3_t_cylindrical(red_word)
    elif questionId == "1387093" and len(red_word) == 4:
        return p6_3_v_t_d(red_word)
    elif questionId == "1290782" and len(red_word) == 3:
        return p6_3_v_t_j(red_word)
    elif questionId == "1816540" and len(red_word) == 3:
        return p6_3_v_napkin(red_word)
    elif questionId == "1290260" and len(red_word) == 3:
        return p6_3_v_t_kh(red_word)
    elif questionId == "1290903" and len(red_word) == 3:
        return p6_3_v_t_sqrt01(red_word)

    elif questionId == "709019" and len(red_word) == 9:
        return p6_4_z_fww(red_word)
    elif questionId == "1816123" and len(red_word) == 3:
        return p6_4_ft(red_word)
    elif questionId == "1816975" and len(red_word) == 6:
        return p6_4_work_spring_a2(red_word)
    elif questionId == "1816443" and len(red_word) == 5:
        return p6_4_work_spring_cm(red_word)
    elif questionId == "1817407" and len(red_word) == 2:
        return p6_4_sandbag(red_word)
    elif questionId == "713959" and len(red_word) == 3:
        return p6_4_tank_a_b_c(red_word)
    elif questionId == "1817117" and len(red_word) == 20:
        return p6_4_midpoint(red_word)
    elif questionId == "713941" and len(red_word) == 3:
        return p6_4_select_cable(red_word)
    elif questionId == "1816142" and len(red_word) == 6:
        return p6_4_work_spring_natural(red_word)
    elif questionId == "1291120" and len(red_word) == 5:
        return p6_4_g_cable(red_word)
    elif questionId == "657132" and len(red_word) == 2:
        return p6_4_Newton_Law(red_word)
    elif questionId == "1816293" and len(red_word) == 3:
        return p6_4_work_spring_lb(red_word)
    elif questionId == "657142" and len(red_word) == 5:
        return p6_4_select_bucket(red_word)
    elif questionId == "713964" and len(red_word) == 2:
        return p6_4_lbft(red_word)
    elif questionId == "1816461" and len(red_word) == 3:
        return p6_4_particle(red_word)
    elif questionId == "708944" and len(red_word) == 18:
        return p6_4_g_Hooke(red_word)
    elif questionId == "1875559" and len(red_word) == 3:
        return p6_4_tank_r_R_h(red_word)
    elif questionId == "1387513" and len(red_word) == 3:
        return p6_4_gas(red_word)
    elif questionId == "709743" and len(red_word) == 2:
        return p6_4_qiu2(red_word)
    elif questionId == "1875548" and len(red_word) == 2:
        return p6_4_qiu3(red_word)
    elif questionId == "713946" and len(red_word) == 5:
        return p6_4_s_cm(red_word)
    elif questionId == "713945" and len(red_word) == 2:
        return p6_4_sandbag(red_word)
    elif questionId == "713945" and len(red_word) == 3:
        return p6_4_sandbag2(red_word)
    elif questionId == "1816384" and len(red_word) == 2:
        return p6_4_T(red_word)
    elif questionId == "3693039" and len(red_word) == 3:
        return p6_4_rope_ab(red_word)
    elif questionId == "713952" and len(red_word) == 3:
        return p6_4_s_cable(red_word)


    elif questionId == "1387419" and len(red_word) == 3:
        return p6_5_ave_t_12(red_word)
    elif questionId == "1816136" and len(red_word) == 3:
        return p6_5_average_exp(red_word)
    elif questionId == "1817078":
        return p6_5_ave_t_sec(red_word)
    elif questionId == "1387600" and len(red_word) == 2:
        return p6_5_average_sin(red_word)
    elif questionId == "1817088" and len(red_word) == 4:
        return p6_5_average_sqrt(red_word)
    elif questionId == "1290484" and len(red_word) == 7:
        return p6_5_g_ba(red_word)
    elif questionId == "1816325" and len(red_word) == 7:
        return p6_5_average_Midpoint(red_word)
    elif questionId == "1816545" and len(red_word) == 3:
        return p6_5_average_density(red_word)
    elif questionId == "1816414" and len(red_word) == 4:
        return p6_5_ave_b(red_word)
    elif questionId == "657280" and len(red_word) == 3:
        return p6_5_ave_t_sqrt(red_word)
    elif questionId == "713970" and len(red_word) == 5:
        return p6_5_ave_s_2(red_word)
    elif questionId == "713950" and len(red_word) == 3:
        return p6_5_ave_t_d2(red_word)
    elif questionId == "1387344" and len(red_word) == 4:
        return p6_5_ave_t_f1(red_word)
    elif questionId == "708939" and len(red_word) == 10:
        return p6_5_ave_z(red_word)

    elif questionId == "1817362" and len(red_word) == 1:
        return p7_1_int_cosh(red_word)
    elif questionId == "1816396" and len(red_word) == 2:
        return p7_1_int_log_sqrt(red_word)
    elif questionId == "1816993" and len(red_word) == 2:
        return p7_1_int_t_sin(red_word)
    elif questionId == "1817186" and len(red_word) == 2:
        return p7_1_int_log(red_word)
    elif questionId == "1816749" and len(red_word) == 1:
        return p7_1_int_dexp(red_word)
    elif questionId == "1817546" and len(red_word) == 1:
        return p7_1_int_cos(red_word)
    elif questionId == "1816409" and len(red_word) == 2:
        return p7_1_int_tcos(red_word)
    elif questionId == "1816692" and len(red_word) == 1:
        return p7_1_int_ze(red_word)
    elif questionId == "1290007" and len(red_word) == 1:
        return p7_1_area_log(red_word)
    elif questionId == "1817420" and len(red_word) == 2:
        return p7_1_int_e(red_word)


    elif questionId == "1817515" and len(red_word) == 2:
        return p7_3_int_x_sqrt(red_word)
    elif questionId == "1816336" and len(red_word) == 2:
        return p7_3_int_dsqrt(red_word)
    elif questionId == "1816637" and len(red_word) == 3:
        return p7_3_int_x_d32(red_word)
    elif questionId == "1817280" and len(red_word) == 1:
        return p7_3_int_sqrtd(red_word)


    elif questionId == "1816994" and len(red_word) == 2:
        return p7_4_int_log2(red_word)
    elif questionId == "1817475" and len(red_word) == 3:
        return p7_4_area(red_word)
    elif questionId == "1816408" and len(red_word) == 3:
        return p7_4_volume_xy(red_word)
    elif questionId == "1817029" and len(red_word) == 2:
        return p7_4_int_dd(red_word)
    elif questionId == "1816838" and len(red_word) == 5:
        return p7_4_int_3dd(red_word)
    elif questionId == "1817374" and len(red_word) == 4:
        return p7_4_int_xd(red_word)
    elif questionId == "1817474" and len(red_word) == 5:
        return p7_4_int_xd2(red_word)
    elif questionId == "1817242" and len(red_word) == 4:
        return p7_4_int_x2d(red_word)
    elif questionId == "1816276" and len(red_word) == 3:
        return p7_4_int_dt2(red_word)
    elif questionId == "1816838" and len(red_word) == 4:
        return p7_4_int_x3d(red_word)
    elif questionId == "1816375" and len(red_word) == 2:
        return p7_4_int_x3d2(red_word)
    elif questionId == "1816354" and len(red_word) == 1:
        return [str(int(red_word[0])*3)]
    elif questionId == "1816812" and len(red_word) == 5:
        return p7_4_int_3d4(red_word)
    elif questionId == "1291147" and len(red_word) == 2:
        return p7_4_int_t_d3(red_word)
    elif questionId == "657245" and len(red_word) == 4:
        return p7_4_int_s_2d3(red_word)
    elif questionId == "1290159" and len(red_word) == 10:
        return p7_4_int_z_2d3(red_word)


    elif questionId == "1816956" and len(red_word) == 3:
        return p7_5_int_power(red_word)
    elif questionId == "1817083" and len(red_word) == 3:
        return p7_5_int_rlog(red_word)
    elif questionId == "1817074" and len(red_word) == 1:
        return p7_5_int_dsqrt(red_word)
    elif questionId == "1816954" and len(red_word) == 3:
        return p7_5_int_1dsqrt(red_word)
    elif questionId == "1816072" and len(red_word) == 2:
        return p7_5_int_dxsqrt(red_word)
    elif questionId == "1816621" and len(red_word) == 2:
        return p7_5_int_bsin(red_word)
    elif questionId == "1816197" and len(red_word) == 2:
        return p7_5_int_nx(red_word)
    elif questionId == "1817208" and len(red_word) == 3:
        return p7_5_int_d(red_word)
    elif questionId == "1817489" and len(red_word) == 2:
        return p7_5_int_dx2sqrt(red_word)
    elif questionId == "1817026" and len(red_word) == 3:
        return p7_5_int_abs(red_word)
    elif questionId == "1817549" and len(red_word) == 2:
        return p7_5_int_dx4a(red_word)
    elif questionId == "1816415" and len(red_word) == 2:
        return p7_5_int_dsqrt(red_word)
    elif questionId == "1817377" and len(red_word) == 2:
        return p7_5_int_dsqrtlog(red_word)
    elif questionId == "1817512" and len(red_word) == 2:
        return p7_5_int_sin2(red_word)
    elif questionId == "1817269" and len(red_word) == 2:
        return p7_5_int_dx4(red_word)
    elif questionId == "1817123" and len(red_word) == 2:
        return p7_5_int_expsqrt(red_word)
    elif questionId == "1817197" and len(red_word) == 4:
        return p7_5_int_x2d2(red_word)
    elif questionId == "1816568" and len(red_word) == 3:
        return p7_5_dint_td2(red_word)
    elif questionId == "1816226" and len(red_word) == 2:
        return p7_5_int_cossin2(red_word)
    elif questionId == "1817348" and len(red_word) == 2:
        return p7_5_int_dxx2(red_word)
    elif questionId == "1816564" and len(red_word) == 2:
        return p7_5_int_dxsqrtd(red_word)
    elif questionId == "1817341" and len(red_word) == 3:
        return p7_5_int_eatan(red_word)
    elif questionId == "1817334" and len(red_word) == 3:
        return p7_5_int_redxe(red_word)
    elif questionId == "1816033" and len(red_word) == 3:
        return p7_5_int_redsqrt(red_word)
    elif questionId == "1817336" and len(red_word) == 5:
        return p7_5_int_t_1d2(red_word)
    elif questionId == "1817336" and len(red_word) == 4:
        return ['enter 5 number and cal, up to down, left to right']
    elif questionId == "1816607" and len(red_word) == 1:
        return p7_5_int_atan(red_word)
    elif questionId == "3860777" and len(red_word) == 1:
        return p7_5_int_sinsqrt(red_word)
    elif questionId == "1816337" and len(red_word) == 1:
        return p7_5_int_cc3sin(red_word)
    elif questionId == "1289877" and len(red_word) == 3:
        return p7_5_int_t_csccot(red_word)

    elif questionId == "1386798" and len(red_word) == 1:
        return p7_7_tm_cos2(red_word)
    elif questionId == "1386708" and len(red_word) == 6:
        return p7_7_tms_t_fu(red_word)
    elif questionId == "872861" and len(red_word) == 13:
        return p7_7_midnight06(red_word)
    elif questionId == "1816754" and len(red_word) == 2:
        return p7_7_simpson_large_n(red_word)
    elif questionId == "1816525" and len(red_word) == 1:
        return p7_7_TMS_f5(red_word)
    elif questionId == "1816656" and len(red_word) == 2:
        return p7_7_TMS_flog(red_word)
    elif questionId == "1816931" and len(red_word) == 7:
        return p7_7_simpson_point18(red_word)
    elif questionId == "1290781" and len(red_word) == 7:
        return p7_7_g_TM(red_word)
    elif questionId == "1817402" and len(red_word) == 1:
        return p7_7_TMS_flogd(red_word)
    elif questionId == "1386639" and len(red_word) == 10:
        return p7_7_simpson_point_gun(red_word)
    elif questionId == "1816261" and len(red_word) == 1:
        return p7_7_TMS_f_plus_sin(red_word)
    elif questionId == "1816154" and len(red_word) == 1:
        return p7_7_TM_f_plus_exp(red_word)
    elif questionId == "1817012" and len(red_word) == 1:
        return p7_7_TMS_sqrtsqrt(red_word)
    elif questionId == "1817527" and len(red_word) == 2:
        return p7_7_TMS_sqrtexp(red_word)
    elif questionId == "1816426" and len(red_word) == 2:
        return p7_7_TMS_cosd(red_word)
    elif questionId == "872859" and len(red_word) == 12:
        return p7_7_midpoint(red_word)
    elif questionId == "1816168" and len(red_word) == 1:
        return p7_7_LRTM_xexp(red_word)
    elif questionId == "657300" and len(red_word) == 2:
        return p7_7_s_mnexp(red_word)
    elif questionId == "657256" and len(red_word) == 2:
        return p7_7_t_cossqrt(red_word)
    elif questionId == "872854" and len(red_word) == 3:
        return p7_7_t_sinexp(red_word)

    elif questionId == "1816794" and len(red_word) == 3:
        return p8_1_manufacturer(red_word)
    elif questionId == "1816649" and len(red_word) == 4:
        return p8_1_length_arc_x(red_word)
    elif questionId == "1816283" and len(red_word) == 4:
        return p8_1_length_arc_xcosh(red_word)
    elif questionId == "780462" and len(red_word) == 3:
        return p8_1_s_len(red_word)
    elif questionId == "1387035" and len(red_word) == 3:
        return p8_1_s_len_kh(red_word)

    elif questionId == "837532" and len(red_word) == 1:
        return p8_2_surface_s_exp(red_word)
    elif questionId == "1817456" and len(red_word) == 1:
        return p8_2_surface_area_rotate_exp(red_word)
    elif questionId == "1291672" and len(red_word) == 1:
        return p8_2_surface_area_xp(red_word)
    elif questionId == "837537" and len(red_word) == 3:
        return p8_2_surface_s_x2(red_word)
    elif questionId == "1290715" and len(red_word) == 2:
        return p8_2_group(red_word)

    elif questionId == "806464" and len(red_word) == 7:
        return p8_3_hydrostatic_simpson(red_word)
    elif questionId == "806449" and len(red_word) == 3:
        return p8_3_hydrostatic_J_ft(red_word)
    elif questionId == "806453" and len(red_word) == 3:
        return p8_3_center_points_x_axis(red_word)
    elif questionId == "806471" and len(red_word) == 12:
        return p8_3_center_points_f11(red_word)
    elif questionId == "806432" and len(red_word) == 3:
        return p8_3_f_point(red_word)
    elif questionId == "1817264" and len(red_word) == 4:
        return p8_3_hydrostatic_swimming(red_word)
    elif questionId == "1816412" and len(red_word) == 2:
        return p8_3_hydrostatic_S(red_word)
    elif questionId == "1816489" and len(red_word) == 3:
        return p8_3_hydrostatic_fx(red_word)
    elif questionId == "1816582" and len(red_word) == 3:
        return p8_3_dam_30du(red_word)
    elif questionId == "837534" and len(red_word) == 2:
        return p8_3_torus(red_word)
    elif questionId == "837530" and len(red_word) == 9:
        return p8_3_s_center(red_word)
    elif questionId == "1386954" and len(red_word) == 9:
        return p8_3_s_center(red_word)
    elif questionId == "874422" and len(red_word) == 4:
        return p8_3_s_T2(red_word)
    elif questionId == "1289984" and len(red_word) == 12:
        return p8_3_z_dam(red_word)

    elif questionId == "1288001" and len(red_word) == 2:
        return p10_1_equ_cosh(red_word)
    elif questionId == "1289426" and len(red_word) == 5:
        return p10_1_equ_t(red_word)
    elif questionId == "817196" and len(red_word) == 3:
        return p10_1_k_sincos(red_word)
    elif questionId == "1288494" and len(red_word) == 1:
        return p10_1_para_sqrt(red_word)
    elif questionId == "1289451" and len(red_word) == 5:
        return p10_1_para_t2(red_word)
    elif questionId == "1288664" and len(red_word) == 4:
        return p10_1_a_b(red_word)

    elif questionId == "807879" and len(red_word) == 3:
        return p10_2_point_slope(red_word)
    elif questionId == "807950" and len(red_word) == 2:
        return p10_2_point_h_v_t3t2(red_word)
    elif questionId == "807937" and len(red_word) == 2:
        return p10_2_point_h_v_t2t3(red_word)
    elif questionId == "1288459" and len(red_word) == 1:
        return p10_2_diff_yin_d(red_word)
    elif questionId == "807959" and len(red_word) == 2:
        return p10_2_rightmost_point(red_word)
    elif questionId == "1289668" and len(red_word) == 1:
        return p10_2_3_e(red_word)
    elif questionId == "807879" and len(red_word) == 4:
        return p10_2_point_slope4(red_word)
    elif questionId == "1289510" and len(red_word) == 3:
        return p10_2_dis_ab(red_word)
    elif questionId == "837513" and len(red_word) == 2:
        return p10_2_s_tan_st(red_word)
    elif questionId == "1288214" and len(red_word) == 3:
        return p10_2_len_exp(red_word)
    elif questionId == "2318454" and len(red_word) == 2:
        return ['enter 3 number and cal']
    elif questionId == "2318454" and len(red_word) == 3:
        return p10_2_len_rt_exp(red_word)
    elif questionId == "837510" and len(red_word) == 2:
        return p10_2_s_kh_sin(red_word)
    elif questionId == "1289735" and len(red_word) == 2:
        return p10_2_len_sqrt(red_word)
    elif questionId == "1289802" and len(red_word) == 2:
        return p10_2_area_texp(red_word)

    elif questionId == "1288092" and len(red_word) == 2:
        return p10_4_oneloop_cos(red_word)
    
    elif questionId == "807252" and len(red_word) == 3:
        return p11_1_a1_5_f1(red_word)

    elif questionId == "1582151" and len(red_word) == 3:
        return p11_2_sum_dn(red_word)
    elif questionId == "1581990" and len(red_word) == 3:
        return p11_2_t_sum_dnkh(red_word)
    elif questionId == "1581991" and len(red_word) == 1:
        return p11_2_t_sum_c(red_word)
    elif questionId == "837576" and len(red_word) == 13:
        return p11_2_s_xs2f(red_word)
    elif questionId == "1581886" and len(red_word) == 2:
        return p11_2_t_consum_d(red_word)
    elif questionId == "1582283" and len(red_word) == 2:
        return p11_2_t_sum_d(red_word)

    elif questionId == "3799075" and len(red_word) == 3:
        return p01_fxx2(red_word)
    elif questionId == "3799116" and len(red_word) == 4:
        return p01_domain3d2(red_word)
    elif questionId == "3798618" and len(red_word) == 1:
        return p01_DRsqrt(red_word)
    elif questionId == "3799103" and len(red_word) == 6:
        return p01_piecewise1(red_word)
    elif questionId == "3798614" and len(red_word) == 1:
        return p01_rectangle(red_word)
    elif questionId == "3799249" and len(red_word) == 2:
        return p01_Biologists(red_word)
    elif questionId == "3799328" and len(red_word) == 2:
        return p01_domain4z_sqrt(red_word)
    elif questionId == "3798734" and len(red_word) == 2:
        return p01_domain4o_d(red_word)
    elif questionId == "3799232" and len(red_word) == 2:
        return p01_ssqrt(red_word)
    elif questionId == "3798905":
        return p01_sabs()
    elif questionId == "3799405":
        return p01_sd2()
    elif questionId == "3798232":
        return p01_sfgh()
    elif questionId == "3798858":
        return p01_scosdsin()
    elif questionId == "3799234":
        return p01_gsqrt(red_word)
    

    elif questionId == "3806078" and len(red_word) == 1:
        return p02_degrees(red_word)
    elif questionId == "3806319" and len(red_word) == 2:
        return p02_trigonometric_sin(red_word)
    elif questionId == "3806062" and len(red_word) == 3:
        return p02_length_abx(red_word)
    elif questionId == "3806092" and len(red_word) == 1:
        return p02_trigonometric_cos(red_word)
    elif questionId == "3806472":
        return p02_du()
    elif questionId == "3805869":
        return p02_qdu()
    elif questionId == "3805882":
        return p02_du6()
    elif questionId == "3806075":
        return p02_degrees_sinsec(red_word)
    elif questionId == "3805947":
        return p02_scos()
    elif questionId == "3806219" and len(red_word) == 2:
        return p02_solvecos(red_word)
    elif questionId == "3806478" and len(red_word) == 2:
        return p02_solvesin(red_word)
    elif questionId == "3805921" and len(red_word) == 2:
        return p02_solvesin2(red_word)    

    elif questionId == "3798732" and len(red_word) == 3:
        return p03_zdsqrt(red_word)
    elif questionId == "3798913" and len(red_word) == 2:
        return p03_by3(red_word)  
    elif questionId == "3799410":
        return p03_z()
    elif questionId == "3798369" and len(red_word) == 2:
        return p03_e4(red_word)  
    elif questionId == "3799425":
        return p03_gdoubling(red_word)
    elif questionId == "3798773":
        return p03_hh()
    elif questionId == "3798293" and len(red_word) == 4:
        return p03_cbx(red_word)

    elif questionId == "3799445" and len(red_word) == 2:
        return p04_log(red_word)
    elif questionId == "3799338" and len(red_word) == 3:
        return p04_logadd(red_word)
    elif questionId == "3799080" and len(red_word) == 4:
        return p04_solve_e(red_word)
    elif questionId == "3798643":
        return p04_sfig()
    elif questionId == "3799190":
        return p04_slog()
    elif questionId == "3801612":
        return p05_ave_v_gtank(red_word)
    elif questionId == "3800905":
        return p05_smlimit()
    elif questionId == "3802006":
        return p05_s3limit()
    elif questionId == "3801715":
        return p05_soo()
    elif questionId == "3801996":
        return p05_soolog()

    elif questionId == "3801214" and len(red_word) == 5:
        return p05_cardiac(red_word)
    elif questionId == "3801808" and len(red_word) == 2:
        return p05_ave_v(red_word)
    elif questionId == "3801322" and len(red_word) == 2:
        return p05_ave_v_sin(red_word)

    elif questionId == "3801556" and len(red_word) == 3:
        return p06_limit_t4(red_word)
    elif questionId == "3801516" and len(red_word) == 4:
        return p06_limit_x2(red_word)
    elif questionId == "3801973" and len(red_word) == 3:
        return p06_limit_t2(red_word)
    elif questionId == "3801497" and len(red_word) == 1:
        return p06_limit_h2(red_word)
    elif questionId == "3803229" and len(red_word) == 2:
        return p06_limit_sqrt(red_word)
    elif questionId == "3802375" and len(red_word) == 2:
        return p06_limit_dd(red_word)
    elif questionId == "3802801" and len(red_word) == 2:
        return p06_limit_h1(red_word)
    elif questionId == "3803094" and len(red_word) == 2:
        return p06_limit_dt2(red_word)
    elif questionId == "3802637" and len(red_word) == 3:
        return p06_limit_sqrtx2(red_word)
    elif questionId == "3801443" and len(red_word) == 12:
        return ['enter 13 number and cal, up to down, left to right']
    elif questionId == "3801443" and len(red_word) == 13:
        return p06_a_f(red_word)
    elif questionId == "3801556" and len(red_word) == 2:
        return ['enter 3 number and cal, up to down, left to right']
    elif questionId == "3801556" and len(red_word) == 3:
        return p06_limit_t42(red_word)

    elif questionId == "3802184" and len(red_word) == 5:
        return p07_limit_fx12(red_word)
    elif questionId == "3802802" and len(red_word) == 4:
        return p07_limit_fx4(red_word)
    elif questionId == "3802327" and len(red_word) == 5:
        return p07_limit_abs(red_word)
    elif questionId == "3803249" and len(red_word) == 2:
        return p07_limit_gx4(red_word)
    elif questionId == "3802908" and len(red_word) == 2:
        return p07_limit_sfx(red_word)
    elif questionId == "3802511" and len(red_word) == 2:
        return p07_limit_t4cos(red_word)

    elif questionId == "3802700" and len(red_word) == 5:
        return p08_continuous2(red_word)
    elif questionId == "3802708" and len(red_word) == 5:
        return p08_continuous_fg(red_word)
    elif questionId == "3803008" and len(red_word) == 15:
        return p08_continuous4(red_word)

    elif questionId == "3802709" and len(red_word) == 3:
        return p09_limitd(red_word)
    elif questionId == "3802589" and len(red_word) == 2:
        return p09_limitd2(red_word)
    elif questionId == "3802441" and len(red_word) == 1:
        return p09_limit_sqrt2d(red_word)
    elif questionId == "3802229" and len(red_word) == 2:
        return p09_limit_sqrt2(red_word)
    elif questionId == "3802168" and len(red_word) == 2:
        return p09_limit_sqrt2_(red_word)        
    elif questionId == "3802687" and len(red_word) == 3:
        return p09_limit_ed(red_word)  
    elif questionId == "4049834" and len(red_word) == 3:
        return p09_limit_xxy(red_word)  

    elif questionId == "3802554" and len(red_word) == 2:
        return p10_ave_v4b(red_word)  
    elif questionId == "3802953" and len(red_word) == 3:
        return p10_diff2(red_word)  
    elif questionId == "3802196" and len(red_word) == 28:
        return p10_g_limit(red_word)  
    elif questionId == "3802340" and len(red_word) == 1:
        return p10_vdt2(red_word)  
    elif questionId == "3802258" and len(red_word) == 10:
        return p10_solpe_point_fig(red_word)  
    elif questionId == "3945586" and len(red_word) == 4:
        return p10_tangent(red_word)  
    elif questionId == "3802527" and len(red_word) == 7:
        return p10_tangent(red_word) 
    elif questionId == "3802933" and len(red_word) == 33:
        return p10_g_ball(red_word) 
    elif questionId == "3802717" and len(red_word) == 2:
        return ['most long, most long, dec, inc']

    elif questionId == "3803115" and len(red_word) == 1:
        return p11_definition(red_word) 
    elif questionId == "3802756" and len(red_word) == 6:
        return p11_table(red_word) 
    elif questionId == "3802394" and len(red_word) == 3:
        return p11_diff12(red_word) 

    elif questionId == "3802582" and len(red_word) == 2:
        return p12_tangent_line(red_word) 
    elif questionId == "3803017" and len(red_word) == 3:
        return p12_d2f(red_word) 
    elif questionId == "3802261" and len(red_word) == 2:
        return p12_va(red_word) 
    elif questionId == "3802644" and len(red_word) == 4:
        return p12_horizontal(red_word) 
    elif questionId == "3802374" and len(red_word) == 4:
        return p12_diffgpx(red_word) 
    elif questionId == "3802638" and len(red_word) == 1:
        return p12_diffgpxkh(red_word) 

    elif questionId == "3802133" and len(red_word) == 1:
        return p13_derivative2(red_word) 
    elif questionId == "3802576" and len(red_word) == 2:
        return p13_diff_exp(red_word) 
    elif questionId == "3803073" and len(red_word) == 1:
        return p13_diff_dexp(red_word) 
    elif questionId == "3802910" and len(red_word) == 1:
        return p13_sqrtd(red_word) 
    elif questionId == "3802304" and len(red_word) == 3:
        return p13_d2d(red_word) 
    elif questionId == "3802691" and len(red_word) == 3:
        return ['enter 4 number and cal, up to down, left to right']
    elif questionId == "3802691" and len(red_word) == 4:
        return p13_difffg(red_word) 
    elif questionId == "3802412" and len(red_word) == 4:
        return ['max*fp+', 'fp-max/', 'f-/', '... ... -max/']

    elif questionId == "3802550" and len(red_word) == 2:
        return p14_tangent_line(red_word) 
    elif questionId == "3802430" and len(red_word) == 1:
        return p14_ecos(red_word) 
    elif questionId == "3803269" and len(red_word) == 2:
        return p14_limit_sind(red_word) 
    elif questionId == "3802920" and len(red_word) == 2:
        return p14_limit_cosdsin(red_word) 
    elif questionId == "3802758" and len(red_word) == 1:
        return ['enter 2 number and cal, up to down, left to right']
    elif questionId == "3802758" and len(red_word) == 2:
        return p14_difffgsc(red_word) 
    elif questionId == "3802146" and len(red_word) == 2:
        return p14_diffbig(red_word) 

    elif questionId == "3802154" and len(red_word) == 2:
        return p15_gfu(red_word) 
    elif questionId == "3803187" and len(red_word) == 2:
        return p15_d34(red_word) 
    elif questionId == "3802659" and len(red_word) == 3:
        return p15_dt32(red_word) 
    elif questionId == "3803102" and len(red_word) == 1:
        return p15_dsqrtd(red_word) 
    elif questionId == "3802373" and len(red_word) == 1:
        return p15_tangent_sinsin(red_word) 
    elif questionId == "3803207" and len(red_word) == 2:
        return p15_diffz(red_word)
    elif questionId == "3802871" and len(red_word) == 11:
        return p15_diffz(red_word)

    elif questionId == "3802313" and len(red_word) == 2:
        return p16_implicitxy(red_word) 
    elif questionId == "3802767" and len(red_word) == 2:
        return p16_implicit2(red_word) 
    elif questionId == "3802652" and len(red_word) == 3:
        return p16_xfx(red_word) 
    elif questionId == "3802789" and len(red_word) == 1:
        return p16_tangent_sincos(red_word) 
    elif questionId == "3803007" and len(red_word) == 2:
        return p16_d2xy(red_word) 

    elif questionId == "3802359" and len(red_word) == 3:
        return p17_diff_ln(red_word) 
    elif questionId == "3802422" and len(red_word) == 1:
        return p17_diff_lnsin(red_word) 
    elif questionId == "3802455" and len(red_word) == 1:
        return p17_diff_lnd(red_word) 
    elif questionId == "3802505" and len(red_word) == 1:
        return p17_diff_lnln(red_word) 
    elif questionId == "3802619" and len(red_word) == 1:
        return p17_diff_ln2(red_word) 
    elif questionId == "3803196" and len(red_word) == 2:
        return p17_tangent_ln(red_word) 
    elif questionId == "3802354" and len(red_word) == 1:
        return p17_diff_sqrtz(red_word) 
    
    elif questionId == "4020903" and len(red_word) == 2:
        return p18_particle(red_word) 
    elif questionId == "3802172" and len(red_word) == 4:
        return p18_height(red_word) 
    elif questionId == "3802914" and len(red_word) == 3:
        return p18_sodium(red_word) 
    elif questionId == "3802972" and len(red_word) == 3:
        return p18_spherical(red_word) 
    elif questionId == "3802475" and len(red_word) == 4:
        return p18_cost(red_word) 
    elif questionId == "3802496" and len(red_word) == 16:
        return p18_gtank(red_word) 
    elif questionId == "3803105" and len(red_word) == 5:
        return p18_Newton_Law(red_word) 

    elif questionId == "3803074" and len(red_word) == 4:
        return p19_gawl(red_word) 
    elif questionId == "3802716" and len(red_word) == 1:
        return p19_oil(red_word) 
    elif questionId == "3802916" and len(red_word) == 2:
        return p19_sphere(red_word)
    elif questionId == "3802439" and len(red_word) == 8:
        return p19_gcars(red_word)
    elif questionId == "3802804" and len(red_word) == 1:
        return p19_gspotlight(red_word)
    elif questionId == "3803623" and len(red_word) == 4:
        return p19_trough(red_word)
    elif questionId == "3804351" and len(red_word) == 2:
        return p19_gravel(red_word)

    elif questionId == "3803795" and len(red_word) == 2:
        return p20_critical3(red_word)
    elif questionId == "3803840" and len(red_word) == 13:
        return p20_gd2(red_word)
    elif questionId == "3803479" and len(red_word) == 2:
        return p20_criticale(red_word)
    elif questionId == "3803364" and len(red_word) == 2:
        return p20_absm(red_word)
    elif questionId == "3803547" and len(red_word) == 2:
        return p20_absd2(red_word)

    elif questionId == "3804512" and len(red_word) == 1:
        return p21_ln(red_word)
    elif questionId == "3803693" and len(red_word) == 1:
        return p21_sqrt(red_word)
    elif questionId == "3803844" and len(red_word) == 6:
        return p21_f_f(red_word)

    elif questionId == "3804353" and len(red_word) == 3:
        return p22_shape3(red_word)
    elif questionId == "3803428" and len(red_word) == 3:
        return p22_local3(red_word)
    elif questionId == "3803471" and len(red_word) == 3:
        return p22_criticalabc(red_word)
    
    elif questionId == "3803963" and len(red_word) == 4:
        return p23_limit2d(red_word)
    elif questionId == "3804132" and len(red_word) == 1:
        return p23_limitsind(red_word)
    elif questionId == "3803863" and len(red_word) == 18:
        return p23_glnd_sqrt(red_word)
    elif questionId == "3804474" and len(red_word) == 3:
        return p23_edsin(red_word)
    elif questionId == "3803997" and len(red_word) == 1:
        return p23_xsin(red_word)
    elif questionId == "3803945" and len(red_word) == 2:
        return p23_cotsin(red_word)
    elif questionId == "3803548" and len(red_word) == 2:
        return p23_ddln(red_word)

    elif questionId == "3804422" and len(red_word) == 1:
        return p25_product(red_word)
    elif questionId == "3803834" and len(red_word) == 6:
        return p25_rectangle(red_word)
    elif questionId == "3803326" and len(red_word) == 1:
        return p25_farmer(red_word)
    elif questionId == "3804348" and len(red_word) == 5:
        return p25_gmanager(red_word)
    elif questionId == "3804481" and len(red_word) == 24:
        return p25_gclosest(red_word)

    elif questionId == "3803474" and len(red_word) == 1:
        return p26_farmer(red_word)
    elif questionId == "3804559" and len(red_word) == 2:
        return p26_point1(red_word)
    elif questionId == "3803663" and len(red_word) == 3:
        return p26_poster(red_word)
    elif questionId == "3803505" and len(red_word) == 3:
        return p26_posterbs(red_word)

    elif questionId == "3804261" and len(red_word) == 15:
        return p27_gnewton(red_word)
    elif questionId == "3804390" and len(red_word) == 1:
        return p27_newton4(red_word)
    elif questionId == "3804482" and len(red_word) == 3:
        return p27_correct(red_word)
    elif questionId == "3803676" and len(red_word) == 1:
        return p27_roote(red_word)
    elif questionId == "3803707" and len(red_word) == 4:
        return p27_gmaximize(red_word)

    elif questionId == "3804246" and len(red_word) == 2:
        return p28_int2(red_word)
    elif questionId == "3804459" and len(red_word) == 6:
        return p28_intzf(red_word)
    elif questionId == "3804286" and len(red_word) == 1:
        return p28_sqrt2(red_word)
    elif questionId == "3803468" and len(red_word) == 1:
        return p28_secte(red_word)
    elif questionId == "3804460" and len(red_word) == 1:
        return p28_4d3(red_word)
    elif questionId == "3803635" and len(red_word) == 3:
        return p28_321(red_word)
    elif questionId == "3804168" and len(red_word) == 2:
        return p28_int1_sqrt(red_word)
    elif questionId == "3803314" and len(red_word) == 1:
        return p28_int1_sec(red_word)
    elif questionId == "3804295" and len(red_word) == 3:
        return p28_int2_2(red_word)
    elif questionId == "3803815" and len(red_word) == 2:
        return p28_int1_tan(red_word)
    elif questionId == "3804543" and len(red_word) == 8:
        return p28_gmarginal(red_word)

    elif questionId == "3806084" and len(red_word) == 2:
        return p29_sum1(red_word)
    elif questionId == "3806076" and len(red_word) == 1:
        return p29_sum_cos(red_word)
    elif questionId == "3804037" and len(red_word) == 2:
        return p30_r36(red_word)
    elif questionId == "3803873" and len(red_word) == 7:
        return p30_runner(red_word)

    elif questionId == "3803449" and len(red_word) == 7:
        return p31_table39(red_word)
    elif questionId == "3804448" and len(red_word) == 2:
        return p31_dint1(red_word)
    elif questionId == "3804109" and len(red_word) == 7:
        return p31_fgc(red_word)
    
    elif questionId == "3803936" and len(red_word) == 4:
        return p32_dint3(red_word)
    elif questionId == "3803896" and len(red_word) == 2:
        return p32_dintkk(red_word)
    elif questionId == "3804183" and len(red_word) == 2:
        return p32_dinte(red_word)
    elif questionId == "3803452" and len(red_word) == 1:
        return p32_dintdx2(red_word)
    elif questionId == "3804310" and len(red_word) == 1:
        return p32_dintsqrt(red_word)

    elif questionId == "3803494" and len(red_word) == 1:
        return p33_bint_sqrtd(red_word)
    elif questionId == "3803395" and len(red_word) == 3:
        return p33_bint_2d2(red_word)
    elif questionId == "3803692" and len(red_word) == 2:
        return p33_bint_sectan(red_word)
    elif questionId == "3803520" and len(red_word) == 4:
        return p33_dint_kk2(red_word)
    elif questionId == "3804257" and len(red_word) == 2:
        return p33_dint_d2d3(red_word)
    elif questionId == "3804163" and len(red_word) == 2:
        return p33_dint_mz(red_word)
    elif questionId == "3803817" and len(red_word) == 3:
        return p33_dint_particle(red_word)
    elif questionId == "3803857" and len(red_word) == 36:
        return p33_dint_particleacc(red_word)

    elif questionId == "3804364" and len(red_word) == 8:
        return p34_gsubs_2sqrt(red_word)
    elif questionId == "3803343" and len(red_word) == 2:
        return p34_bint_cos(red_word)
    elif questionId == "3803949" and len(red_word) == 1:
        return p34_bint_sinzcos(red_word)
    elif questionId == "3803582" and len(red_word) == 30:
        return p34_bint_gd(red_word)
    elif questionId == "3804276" and len(red_word) == 11:
        return p34_bint_glnz(red_word)
    elif questionId == "3804311" and len(red_word) == 11:
        return p34_bint_gesqrt(red_word)
    elif questionId == "3803819" and len(red_word) == 1:
        return p34_bint_sectan(red_word)
    elif questionId == "3804091" and len(red_word) == 1:
        return p34_bint_sindcos(red_word)
    elif questionId == "3803749" and len(red_word) == 2:
        return p34_dint_ez(red_word)
    elif questionId == "3804396" and len(red_word) == 2:
        return p34_dint_xe(red_word)


    else:
        return ["nocode"]

if __name__ == '__main__':
    questionId = '3806282'
    red_word = '100,800'
    result = doit(questionId,red_word)
    print(result)
    