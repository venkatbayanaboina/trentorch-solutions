import numpy as np


def max_pool_strided(matrix: np.ndarray, k: int, s: int) -> np.ndarray:
    """
    2D max pooling with independent kernel size k and stride s, no padding.

    matrix: shape (H, W).
    k: window size (height and width). s: stride, can differ from k.

    Output shape is (floor((H-k)/s)+1, floor((W-k)/s)+1). Cell (i, j) is the
    max over the window with top-left corner (i*s, j*s), size k x k. Any
    trailing rows/columns that don't fill a full window are dropped, not
    padded.
    """
    # TODO: step each window's start by s, not by k. s and k can differ.
    h , w = np.shape(matrix)
   # k = min(h,w)

    output_window= np.zeros (   (  ((h-k)//s)+1 , ((w-k)//s)+1   )    )

    
    for i in range(0,h-k+1,s):
        window = np.zeros((k,k ))
        for j in range(0,w-k+1,s):
            window= matrix[i:i+k,j:j+k]
            output_window[i // s, j // s] = np.max(window) 
            
            
        
    return output_window
