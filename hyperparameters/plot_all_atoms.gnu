set terminal svg enhanced font "Latin Modern Roman,12" size 1200,900
set output "learning_curves.svg"

set multiplot layout 3,2 title "QM7 Radical Cations - Atomic Charges"

set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u."
set grid

set logscale y

set style line 1 lc rgb "red" lw 2 pt 7 ps 1.5
set style line 2 lc rgb "blue" lw 2 pt 7 ps 1.5
set style line 3 lc rgb "green" lw 2 pt 7 ps 1.5

atoms = "O S N"

do for [i=1:words(atoms)] {
    atom = word(atoms, i)

    set title sprintf("%s", atom)

    plot sprintf("gaussian_mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 1 title "aSPAHM", \
         sprintf("gaussian_mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 2 title "bSPAHM", \
         sprintf("gaussian_mean_MAE_%s_a_slatm.txt", atom) using 1:($2 * 10**2) with linespoints ls 3 title "aSLATM"
}

unset multiplot
set output
set terminal qt

