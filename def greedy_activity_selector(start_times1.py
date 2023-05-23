def greedy_activity_selector(start_times, finish_times):
    n = len(start_times)
    selected_activities = []
    i = 0
    selected_activities.append(i)  # Memilih kegiatan pertama
    
    for j in range(1, n):
        # Memilih kegiatan dengan waktu selesai tercepat yang tidak tumpang tindih dengan kegiatan sebelumnya
        if start_times[j] >= finish_times[i]:
            selected_activities.append(j)
            i = j
    
    return selected_activities

# Contoh penggunaan
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]

selected_activities = greedy_activity_selector(start_times, finish_times)

print("Kegiatan yang dipilih:")
for activity in selected_activities:
    print(f"Kegiatan {activity + 1} (mulai: {start_times[activity]}, selesai: {finish_times[activity]})")
