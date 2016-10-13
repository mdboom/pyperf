import perf.text_runner

mydict = {str(k): k for k in range(1000)}

def func(loops):
    # use a fast local variable to access the dictionary
    local_dict = mydict
    range_it = range(loops)
    t0 = perf.perf_counter()

    for loops in range_it:
        local_dict['0']
        local_dict['100']
        local_dict['200']
        local_dict['300']
        local_dict['400']
        local_dict['500']
        local_dict['600']
        local_dict['700']
        local_dict['800']
        local_dict['900']

    return perf.perf_counter() - t0

runner = perf.text_runner.TextRunner()
# inner-loops: mydict[int] is duplicated 10 times
runner.bench_sample_func('dict[int]', func, inner_loops=10)
