import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    classes = np.unique(np.concatenate([y_true, y_pred]))

    tp_total, fp_total, fn_total = 0, 0, 0

    for c in classes:
        tp_total += np.sum((y_true == c) & (y_pred == c))
        fp_total += np.sum((y_true != c) & (y_pred == c))
        fn_total += np.sum((y_true == c) & (y_pred != c))

    denom = 2 * tp_total + fp_total + fn_total

    return (2 * tp_total / denom).tolist() if denom else 0.0
    pass