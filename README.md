# Transformation-Matrix
This repository calculates the transformation matrix for 2D to 2D projection. In the following we want to explore the projection for a single point and generalize it to multiple points.


$$ \begin{bmatrix} 
   su \\
   sv \\
   s \\
   \end{bmatrix} = 
   \begin{bmatrix}
   m11 & m12 & m13 \\
   m21 & m22 & m23 \\
   m31 & m32 & m33 \\
   \end{bmatrix}*
   \begin{bmatrix}
   X\\
   Y\\
   1\\
   \end{bmatrix}
$$

By matrix multiplication we find the following equations:

```math
su = m11 X + m12Y + m13
```
```math
sv = m21X + m22Y + m23
```
```math
s = m31X + m32Y + m33  (*)
```

We can replace the star equation in equations 1 and 2 and obtain the following:
```math
m11 X + m12Y + m13 - (m31X)u - (m32Y)u - m33u = 0
```
```math
m21X + m22Y + m23 - (m31X)v - (m32Y)v - m33v = 0
```
Intuitively we find that if we have multiple data points, the above equations can be generalized to:

$$ 
   \begin{bmatrix}
   X1 & Y1 & 1 & 0 & 0 & 0 & -u1X1 & -u1Y1 & -u1\\
   0 & 0 & 0 & X1 & Y1 & 1 & -v1X1 & -v1Y1 & -v1\\
   ⋮ & ⋮ & ⋮ & ⋮ & ⋮ & ⋮ & ⋮ & ⋮ & ⋮ &\\
   Xn & Yn & 1 & 0 & 0 & 0 & -UnXn & -UnYn & -Un\\
   0 & 0 & 0 & X1 & Y1 & 1 & -VnXn & -VnYn & -Vn\\
   \end{bmatrix}*
   \begin{bmatrix}
   m11\\
   m12\\
   ⋮ \\
   m32\\
   m33\\
   \end{bmatrix}=
   \begin{bmatrix}
   0\\
   0\\
   ⋮ \\
   0\\
   0\\
   \end{bmatrix}
$$

if we form the above equation as Ax=0 it can be concluded that x=0 is a trivial solution and has to be avoided. It is proved that the following approach will give you the optimum solution:
- Minimize ||Ax|| subject to ||𝐱|| = 1
- Suppose we take the singular value decomposition of A to get A=UΣVT
- If the equation Ax=0 can be solved exactly, then at least one of the eigenvalues of A must be zero. So, if one of elements on the diagonal of Σ is zero, then we have a solution.
- That solution corresponds to the column of V that corresponds to the zero-valued singular value.
- If none of the singular values are zero, we have no solution to our equation. It can be proved that in this case, the smallest singular value corresponds to the solution to the linear least squares fitting problem.






