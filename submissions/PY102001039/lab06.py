# -------------------------
# Do not change the below Code
# -------------------------
def helper_fun1_(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break

    return arr

def helper_fun2_(arr, i):
    n = len(arr)

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            i = smallest
        else:
            break
    return arr

# ------------------------------------------------------------
# Q1 — schedule_next_job
# ------------------------------------------------------------
# A cloud system maintains a job list where each job has a
# priority score (smaller value = higher priority).
#
# The system must always be able to quickly access (O(1)) the job
# with the highest priority (smallest score).
#
# You are given the current job list (arr) and a new job
# (priority_score).
#
# Write a function to add a new job into the system
# and and reorganize the list so that the priority rule is maintained.

# IMPORTANT:
# - You may use the provided helper functions to adjust the structure.
# - Do NOT implement any additional helper functions.
# ------------------------------------------------------------

def schedule_next_job(jobs, new_job):
    # TODO: insert job
    # TODO: move it upward as needed (like heap behavior)
    jobs.append(new_job)

    # print(jobs[-1])
    return helper_fun1_(jobs, len(jobs)-1)
    
    # print(jobs)


# jobs = [4,6,8,11,12]
# new_job = 2
# schedule_next_job(jobs,new_job)
#     
# arr = [12, 29, 76, 31, 65, 80, 77]
# schedule_next_job(arr, 10)

# arr = [12, 29, 76, 31, 65, 80, 77]
# schedule_next_job(arr, 90)

# arr = [12, 29, 76, 31, 65, 80, 77]
# schedule_next_job(arr, 29)

# arr = [20]
# schedule_next_job(arr, 10)


# ------------------------------------------------------------
# Q2 — process_next_job
# ------------------------------------------------------------
# A system processes jobs based on priority score
# (smaller value = higher priority).
#
# The job with the highest priority is always processed first.
#
# Given the current job list (arr), remove and return the
# next job to process.
#
# After removal, reorganize the list to maintain the
# priority rule.
#
# IMPORTANT:
# - You may use the provided helper functions to adjust the structure.
# - Do NOT implement any additional helper functions.
#
# ------------------------------------------------------------

def process_next_job(arr):
    if len(arr) == 0:
        return None

    # TODO: return removed job and updated list

    if not arr:
        return None
    
    removed_job = arr[0]
    last = arr.pop()

    if arr:
        arr[0] = last
        helper_fun2_(arr, 0)

    return removed_job, arr

    # print(arr)

    
        
    #print(arr)

# jobs = [4,6,8,11,12]
# jobs = [4,6,7,8,9,10,11]
# process_next_job(jobs)   

# arr = [12, 29, 76, 31, 65, 80, 77, 90]
# removed, updated = process_next_job(arr)  
# print(removed) 
# print(updated)

# arr = [12, 29, 76, 31, 65, 80, 77, 90]
# removed, updated = process_next_job(arr[:])
# print(removed) 
# print(updated)

# arr = [12]
# removed, updated = process_next_job(arr[:])
# print(removed) 
# print(updated)

# arr = []
# removed, updated = process_next_job(arr[:])
# print(removed) 
# print(updated)

# arr = [5, 10, 20, 30, 40, 50, 60]
# removed, updated = process_next_job(arr[:])
# print(removed) 
# print(updated)
    
# ------------------------------------------------------------
# Q3 — personal priority reflection
# ------------------------------------------------------------
# This question is about reflecting on your personal priorities.
#
# You are given a structure where each item is:
#     (weight, category)
#
# Smaller weight = higher priority.
#
# Instructions:
# 1. Change the weights (numbers) based on YOUR priorities.
# 2. Do NOT change the category names.
# 3. Insert a new category ("security") with your chosen weight.
# 4. Maintain the structure using the provided helper function.
#
# NOTE:
# - There is NO single correct answer.
# - Focus on meaningful weights based on your perspective.
# - Do NOT create additional helper functions.
# ------------------------------------------------------------

def personal_priority_q():
    priorty_q = [
        (10, "education"),
        (2, "family"),
        (6, "health"),
        (4, "friends"),
        (8, "money")
    ]
    # TODO: append new_item to personal_priorty_q
    new_item = (5, "security")


    # TODO: return the list 
    # highest priority (lowest score) should be always top

    for i in range(len(priorty_q)):
        helper_fun1_(priorty_q, i)
    # print(priorty_q)    

    priorty_q.append(new_item)
    helper_fun1_(priorty_q, len(priorty_q) - 1)

    return priorty_q


# priorty_list = personal_priority_q()
# print(priorty_list)

# result = personal_priority_q()
# print(result)
# print(len(result))
# print(all(isinstance(item, tuple) and len(item) == 2 for item in result))
