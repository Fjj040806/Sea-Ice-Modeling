# Connectivity and Fragmentation of Arctic Sea Ice in Satellite Concentration Fields

## Abstract

We study the connectivity and fragmentation of Arctic sea-ice concentration (SIC) fields using NOAA/NSIDC G02202 Version 6 monthly satellite data. The project began by testing whether thresholded SIC exhibits a reproducible finite-domain percolation transition as the concentration threshold varies. Real September fields from 1979 and 2025 do not support that interpretation: over the physically relevant range q = 0.15–0.98, the largest connected component remains dominant, while the strongest apparent transition occurs only near q = 0.99–1.00, where the monthly SIC product is strongly quantized. We therefore reject a physical critical-point interpretation and reformulate the problem around fixed, physically meaningful SIC thresholds. The resulting comparison shows substantially less sea ice in 2025, but a larger fraction of the surviving high-concentration ice belongs to one dominant connected component.

## 1. Research question

Let

$$
C_{ij}(t)\in[0,1]
$$

denote sea-ice concentration in grid cell $(i,j)$ at time $t$. For threshold $q$, define the binary superlevel set

$$
X_q(i,j,t)=\mathbf{1}\{C_{ij}(t)\ge q\}.
$$

The original question was whether the topology of $X_q$ displays a robust transition as $q$ varies. The empirical results show that the near-unity transition is strongly affected by quantization. The revised question is:

**How do the connectivity and fragmentation of Arctic sea ice differ at physically meaningful SIC thresholds, and can these structural quantities contain information beyond total sea-ice area?**

## 2. Data and physical-area weighting

The primary product is NOAA/NSIDC G02202 Version 6 on the Northern Hemisphere 25-km polar-stereographic grid. The two empirical snapshots used here are September 1979 and September 2025. Ocean cells are retained, while land, coast, lakes, and the pole-hole mask category are excluded.

The projected grid has nominal spacing

$$
\Delta x=\Delta y=25\ \mathrm{km}.
$$

Because polar stereographic coordinates are not exactly equal area, raw pixel count is not used as physical area. If $k_{ij}$ is the local conformal map-scale factor, the physical area represented by cell $(i,j)$ is approximated by

$$
a_{ij}=\frac{\Delta x\,\Delta y}{k_{ij}^{2}}.
$$

All area-based connected-component statistics use these weights.

## 3. Graph formulation

For fixed $q$ and $t$, define

$$
V_q(t)=\{(i,j):C_{ij}(t)\ge q\}.
$$

The thresholded sea-ice graph is

$$
G_q(t)=\bigl(V_q(t),E_q(t)\bigr).
$$

Under 4-neighbor connectivity,

$$
(i,j)\sim(i',j')
\Longleftrightarrow
|i-i'|+|j-j'|=1.
$$

Under 8-neighbor connectivity, diagonal contacts are also included:

$$
\max\{|i-i'|,|j-j'|\}=1.
$$

Let the connected components be $\mathcal C_1,\ldots,\mathcal C_{N_q}$. Their physical areas are

$$
S_r(q,t)=\sum_{(i,j)\in\mathcal C_r}a_{ij},
$$

and total thresholded ice area is

$$
A(q,t)=\sum_{r=1}^{N_q}S_r(q,t).
$$

## 4. Connectivity and fragmentation observables

### 4.1 Largest-component fraction

Let

$$
S_{\max}(q,t)=\max_r S_r(q,t).
$$

Define

$$
P_\infty(q,t)=\frac{S_{\max}(q,t)}{A(q,t)}.
$$

Here $P_\infty$ is a finite-domain concentration statistic, not an infinite-lattice probability. Values near one indicate that most thresholded ice belongs to one basin-scale component.

### 4.2 Finite-cluster susceptibility

Let $r^*$ index the largest component and define

$$
M_m(q,t)=\sum_{r\ne r^*}S_r(q,t)^m.
$$

Then

$$
\chi(q,t)
=
\frac{M_2(q,t)}{M_1(q,t)}
=
\frac{\sum_{r\ne r^*}S_r(q,t)^2}
{\sum_{r\ne r^*}S_r(q,t)}.
$$

A localized maximum in $\chi$ is used as an operational diagnostic, not as proof of a thermodynamic critical point.

### 4.3 Cluster entropy

Define component shares

$$
p_r(q,t)=\frac{S_r(q,t)}{A(q,t)}.
$$

The Shannon cluster entropy is

$$
H(q,t)=-\sum_{r=1}^{N_q}p_r\log p_r,
$$

with normalized form

$$
H_{\mathrm{norm}}(q,t)=\frac{H(q,t)}{\log N_q}
$$

for $N_q>1$.

### 4.4 Simpson fragmentation index

We define

$$
F(q,t)=1-\sum_{r=1}^{N_q}p_r(q,t)^2.
$$

$F$ is small when one component dominates and larger when ice area is divided among many similarly sized components.

### 4.5 Boundary complexity

Let $\mathcal E_{\partial}(q,t)$ be neighboring valid-ocean cell pairs whose binary occupancy differs. With representative edge length $\ell_e$,

$$
L_{\partial}(q,t)=\sum_{e\in\mathcal E_{\partial}(q,t)}\ell_e,
$$

and the area-normalized edge density is

$$
D_{\partial}(q,t)=\frac{L_{\partial}(q,t)}{A(q,t)}.
$$

This distinguishes compact connected ice from a more crenulated or perforated region of comparable area.

## 5. Threshold filtration

The superlevel sets are nested:

$$
q_1<q_2
\Longrightarrow
V_{q_2}(t)\subseteq V_{q_1}(t).
$$

Therefore $\{G_q(t)\}$ forms a filtration. As $q$ increases, connected components shrink, split, or disappear. This structure also motivates future persistent-homology analysis.

## 6. Operational transition estimators

The initial transition estimators were

$$
\widehat q_{\mathrm{slope}}
=
\arg\max_q
\left|
\frac{\Delta P_\infty(q,t)}{\Delta q}
\right|
$$

and

$$
\widehat q_{\chi}
=
\arg\max_q\chi(q,t).
$$

A credible finite-domain transition would need to be localized and qualitatively stable across adjacency definitions without being produced by data encoding.

## 7. Quantization and empirical falsification

The decoded monthly SIC field is effectively quantized in increments of 0.01:

$$
C_{ij}\in\{0,0.01,0.02,\ldots,1.00\}.
$$

Let

$$
N_c=\#\{(i,j):C_{ij}=c\}.
$$

When the threshold moves from $q=c$ to $q=c+0.01$, as many as $N_c$ cells can disappear simultaneously. Hence a large finite difference

$$
\Delta P_\infty
=
P_\infty(c+0.01)-P_\infty(c)
$$

can arise from an atomic mass in the empirical SIC distribution rather than a scale-free connectivity phenomenon.

In 1979, the exact ocean-cell counts at SIC 0.98, 0.99, and 1.00 are 2,017, 2,719, and 836. In 2025 they are 1,008, 1,331, and 890. The strongest nominal transition occurs at the same upper-tail values where the quantized field contains large discrete masses.

For 4-neighbor connectivity,

$$
P_\infty(0.98,1979)=0.939,
\qquad
P_\infty(0.98,2025)=0.974.
$$

Across q = 0.15–0.98, the largest component remains dominant in both fields. The original claim of a robust physical q-driven percolation threshold therefore fails the empirical gate.

## 8. Fixed-threshold structural comparison

At q = 0.15,

$$
A(0.15,1979)=6.272\ \mathrm{million\ km}^2,
$$

while

$$
A(0.15,2025)=4.926\ \mathrm{million\ km}^2.
$$

Yet

$$
P_\infty(0.15,1979)=0.960,
\qquad
P_\infty(0.15,2025)=0.974.
$$

At q = 0.80, thresholded area decreases from 4.742 to 3.549 million km². The number of 4-neighbor components falls from

$$
N_{0.80}(1979)=29
$$

to

$$
N_{0.80}(2025)=13,
$$

while

$$
P_\infty(0.80,1979)=0.965,
\qquad
P_\infty(0.80,2025)=0.981.
$$

Thus less high-concentration ice does not imply a more fragmented basin-scale network in these two snapshots.

It is useful to separate ice amount from structural state:

$$
A(q,t)
\quad\text{and}\quad
\mathcal G(q,t)
=
\bigl(
P_\infty,
N_q,
H_{\mathrm{norm}},
F,
D_{\partial},
S_{\max}
\bigr).
$$

There is no mathematical requirement that $\mathcal G(q,t)$ be monotone in $A(q,t)$.

## 9. Full-record statistical model

For a future annual September series $t=1979,\ldots,2025$, let

$$
Y_t(q)
\in
\{
P_\infty,N_q,H_{\mathrm{norm}},F,D_{\partial},S_{\max}
\}.
$$

A first-order trend model is

$$
Y_t(q)
=
\alpha(q)
+
\beta(q)(t-1979)
+
\varepsilon_t(q).
$$

To test whether structural change contains information beyond total ice area, use

$$
Y_t(q)
=
\alpha(q)
+
\beta_1(q)A_t(q)
+
\beta_2(q)t
+
\varepsilon_t(q).
$$

If $\beta_2(q)$ remains meaningfully different from zero after conditioning on $A_t(q)$, the structural observable may capture geometric reorganization not reducible to total-area loss.

A nonlinear extension is

$$
Y_t(q)
=
\alpha(q)+f_q(t)+\gamma(q)A_t(q)+\varepsilon_t(q),
$$

where $f_q$ is a smooth time function.

## 10. Limitations and extensions

Only two September snapshots are analyzed here. They are sufficient to expose the upper-tail quantization problem and show that total area and connectedness need not change in the same direction. They are not sufficient for a multidecadal climate trend, causal attribution, or regime-shift claim.

A full study should process every September field in the satellite record, examine sensitivity to sensor-era changes, and repeat the analysis with an independent SIC product. The filtration structure also suggests persistent homology, in which Betti-0 and Betti-1 features are tracked across threshold rather than summarized by a single operational transition value.

## 11. Conclusion

The candidate monthly-SIC percolation transition is concentrated at the quantized upper tail of G02202 Version 6 and should not be interpreted as a physical critical point. At physically meaningful fixed thresholds, however, the two snapshots reveal a more interesting structural possibility: Arctic sea-ice loss can coexist with a smaller but more dominant connected core. This separates loss of ice from loss of connectedness and provides a stronger basis for a full satellite-era structural-connectivity study.

## Reproducibility

The repository contains the analysis code, derived structural metrics, quantization diagnostics, and display figures. The two raw NOAA/NSIDC NetCDF inputs are public data and are intentionally excluded from version control.
