import time
from concurrent.futures import ThreadPoolExecutor

import httpx


URL = "http://127.0.0.1:8000/predict"
REQUEST_COUNT = 50


def send_request():
    start = time.perf_counter()

    response = httpx.post(
        URL,
        json={"text": "I have high temperature"},
        timeout=30,
    )

    latency = time.perf_counter() - start

    return response.status_code, latency


def main():
    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(lambda _: send_request(), range(REQUEST_COUNT)))

    total_time = time.perf_counter() - start_time

    successful = sum(
        1 for status_code, _ in results if status_code == 200
    )

    latencies = [latency for _, latency in results]

    average_latency = sum(latencies) / len(latencies)
    max_latency = max(latencies)
    min_latency = min(latencies)

    throughput = successful / total_time

    print("=" * 50)
    print("LOAD TEST RESULTS")
    print("=" * 50)
    print(f"Total requests: {REQUEST_COUNT}")
    print(f"Successful requests: {successful}")
    print(f"Failed requests: {REQUEST_COUNT - successful}")
    print(f"Total time: {total_time:.4f} seconds")
    print(f"Average latency: {average_latency:.4f} seconds")
    print(f"Minimum latency: {min_latency:.4f} seconds")
    print(f"Maximum latency: {max_latency:.4f} seconds")
    print(f"Throughput: {throughput:.2f} requests/second")


if __name__ == "__main__":
    main()