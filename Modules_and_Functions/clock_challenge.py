# Write a small program to display
# the information of four clocks we
# just looked at:
# time, perf_counter, monotonic and
#                     process_time
import time

print(time.perf_counter())
print(time.monotonic())
print(time.process_time())
print(time.time())
