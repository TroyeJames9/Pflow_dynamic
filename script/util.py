# -*- coding: utf-8 -*-

"""

这个模块用来存放公用对象和函数

"""
import concurrent.futures

# noinspection PyUnresolvedReferences
import multiprocessing

# noinspection PyPackageRequirements
import psutil


def multipule_process(
    func_name=None,
    arg_list: list = None,
    max_workers: int = psutil.cpu_count(logical=False) // 2,
    chunksize: int = None,
):
    """
    定义一个多进程并发执行函数的包装器multipuleProcess，用于将一个函数func_name应用于arg_list中的参数列表，
    并利用最大进程数max_workers进行并行计算，同时支持自定义分块大小chunksize。

    参数：
    - func_name (Callable): 待并行执行的函数。
    - arg_list (list): 函数func_name需要应用的一系列参数列表。
    - max_workers (int, 默认值为逻辑CPU核心数的一半): 最大进程数，用于限制并发执行的进程数量。
    - chunksize (int, 默认值根据arg_list和max_workers动态计算): 分块大小，用于决定每次分配给进程执行的任务数量。

    功能描述：
    1. 根据max_workers创建一个并发.futures.ProcessPoolExecutor上下文管理器。
    2. 如果chunksize参数未指定，则根据arg_list的长度和max_workers自动计算一个合适的分块大小。
    3. 使用executor.map方法将func_name函数并行应用到arg_list的各个元素上，按照设定的chunksize进行分块处理。
    4. 收集所有并行计算结果，将其整合为一个列表并返回。

    返回：
    - result_list (list): 包含所有并行执行结果的列表，其顺序与arg_list中参数的顺序相对应。

    适用于CPU密集型代码
    """
    # 使用with语句创建并发.futures.ProcessPoolExecutor上下文管理器，保证进程池的正确关闭
    with concurrent.futures.ProcessPoolExecutor(max_workers) as executor:
        # 如果chunksize未指定，则根据arg_list的长度和max_workers计算合理的分块大小
        if chunksize is None:
            chunksize = len(arg_list) // max_workers // 20
            # 确保chunksize至少为1，避免无法进行有效的任务分割
            if chunksize <= 1:
                chunksize = 1

        # 使用executor.map函数将func_name并行应用到arg_list的每个元素上，分块大小为chunksize
        result_list = list(executor.map(func_name, arg_list, chunksize=chunksize))

    return result_list


def multipule_thread(
    func_name=None,
    arg_list: list = None,
    max_workers: int = psutil.cpu_count(logical=True),
):
    """
    定义一个名为multipuleThread的函数，该函数旨在并发地执行用户提供的函数func_name，并将结果收集到一个列表中。
    通过线程池并发处理，提高了执行效率，充分利用多核CPU资源。

    参数：
    - func_name (Callable, 默认None): 需要并发执行的函数对象。
    - arg_list (list, 默认None): 包含多个参数的列表，这些参数将分别传递给func_name函数执行。
    - max_workers (int, 默认psutil.cpu_count(logical=True)): 线程池中最大线程数量，默认为逻辑处理器核心数。

    返回：
    - result_list (list): 包含func_name函数执行完毕后所有结果的列表，其顺序与arg_list中的参数顺序一致。

    适用于I/O密集型代码
    """
    # 使用with语句创建一个线程池Executor上下文管理器，根据max_workers参数初始化线程池大小
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 使用map方法将func_name函数并行地应用到arg_list的每个元素上，并将结果收集到result_list中
        result_list = list(executor.map(func_name, arg_list))

    return result_list
