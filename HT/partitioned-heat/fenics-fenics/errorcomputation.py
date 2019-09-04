from fenics import inner, assemble, dx, project, sqrt

def compute_errors(u_approx, u_ref, V, total_error_tol = 10**-4):
    error_normalized = (u_ref - u_approx)/u_ref  # compute pointwise L2 error
    error_pointwise = project(abs(error_normalized), V)  # project onto function space
    error_total = sqrt(assemble(inner(error_pointwise, error_pointwise) * dx))  # determine L2 norm to estimate total error
    error_pointwise.rename("error", " ")
    try:
        assert (error_total < total_error_tol)
    except AssertionError:
        print("total error is too high! error_total: {}, tolerance: {}".format(error_total, total_error_tol))
        quit(1)

    return error_total, error_pointwise
