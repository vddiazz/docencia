set terminal postscript portrait enhanced color 'Helvetica' 14
#set terminal postscript portrait enhanced color 'Times-Roman' 18

set output '| epstopdf --filter --outfile=paquete_cuadrado_ancho.pdf'
#set output 'paquete_cuadrado.ps'

set size 1.0,0.5

set title 'Paquete de ondas cuadrado a t=0, k_0={/Symbol p}, {/Symbol D}k=0.1k_0'

set label "" at graph 0.3,0.5

set xlabel 'x (m)'
set ylabel 'Amplitud (unidades arbitrarias) '

set key top right 

set key spacing 1.3

set pointsize 0.8

set mxtics 2 
set mytics 2

set grid

#set format y "10^{%T}"

set xrange[-10.:10.]
set yrange[:]

#set logscale x
#set logscale y

f(x,k0,Dk)=2*Dk*cos(k0*x)*sin(Dk*x)/(Dk*x)
g(x,k0,Dk)=2*Dk*sin(Dk*x)/(Dk*x)

k0=2.*pi
Dk=0.1*k0

set samples 1000

plot [x=-10.:10] \
f(x,k0,Dk) ti 'Paquete de ondas' w l lt 1 lw 3 lc rgb "black",\
g(x,k0,Dk) ti 'Envolvente' w l dashtype (3,1) lw 2 lc rgb "red",\
-g(x,k0,Dk) noti 'Envolvente' w l dashtype (3,1) lw 2  lc rgb "red"
