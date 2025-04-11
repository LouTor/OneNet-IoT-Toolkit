from concurrent.futures import ThreadPoolExecutor, as_completed


def execute_tasks(df, task_func, threads: int):
    succ_cnt = 0
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(task_func, row) for _, row in df.iterrows()]
        for future in as_completed(futures):
            try:
                if future.result():
                    succ_cnt += 1
            except Exception as e:
                print(f"错误: {e}")
    return succ_cnt
