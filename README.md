# Transformation-Matrix
This repository calculates the transformation matrix for 2D to 2D projection. In the following we want to explore the projection for a single point and generalize it to multiple points.


$$\begin{bmatrix} 
| su |   |m11 m12 m13|
| sv | = |m21 m22 m23|
| s  |   |m31 m32 m33| \end{bmatrix}$$


```math
  \begin{bmatrix} 
    su \\ 
    sv \\ 
    s
  \end{bmatrix} = 
  
  \begin{bmatrix} 
   
    m11m12  m13\\ 
    m21 m22 m23\\ 
    m31 m32 m33

  \end{bmatrix}
```

