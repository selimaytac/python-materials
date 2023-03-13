import numpy as np

endpoints = np.array(['endpoint1', 'endpoint2', 'endpoint1'])
counts = np.array([10, 5, 3])

unique_endpoints, endpoint_counts = np.unique(endpoints, return_counts=True)

total_counts = np.zeros_like(unique_endpoints, dtype=np.int64)
for i, endpoint in enumerate(unique_endpoints):
    endpoint_mask = (endpoints == endpoint)
    endpoint_values = counts[endpoint_mask]
    total_counts[i] = np.sum(endpoint_values)

print(unique_endpoints)
print(total_counts)

#--------------------------------------------------------------

users = np.array(['User1', 'User2', 'User1', 'User3'])
activities = np.array(['Activity1', 'Activity2', 'Activity3', 'Activity1'])
points = np.array([10, 5, 3, 8])

unique_users, user_points = np.unique(users, return_counts=True)
total_points = np.zeros_like(unique_users, dtype=np.int64)
for i, user in enumerate(unique_users):
    user_mask = (users == user)
    user_activities = activities[user_mask]
    user_points_for_activities = points[user_mask]
    unique_activities, activity_counts = np.unique(user_activities, return_counts=True)
    for j, activity in enumerate(unique_activities):
        activity_mask = (user_activities == activity)
        activity_points = user_points_for_activities[activity_mask]
        total_points[i] += np.sum(activity_points) * activity_counts[j]

print(unique_users)
print(total_points)

#--------------------------------------------------------------

import numpy as np
import multiprocessing as mp

# Büyük boyutlu bir numpy dizisi oluşturma
arr = np.random.rand(10000000)

# İşlemci çekirdeklerinin sayısını al
num_cpus = mp.cpu_count()

# Her bir işlemci çekirdeği için bir alt-dizi boyutu hesapla
chunk_size = int(len(arr) / num_cpus)

# Her bir alt-dizide maksimum değeri hesaplamak için bir işleme işlevi tanımlama
def process_chunk(chunk):
    return np.max(chunk)

# multiprocessing.Pool sınıfını kullanarak işleme işlevlerini işlemek için bir işlem havuzu oluşturma
pool = mp.Pool(processes=num_cpus)

# numpy dizisini alt-dizilere böl ve her bir alt-diziyi işlem havuzunda işle
results = pool.map(process_chunk, [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)])

# İşlem sonuçlarının maksimumunu al
max_result = np.max(results)

print(max_result)
