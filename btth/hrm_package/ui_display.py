def display_records(book):
    if not book:
        print("Chưa có dữ liệu chấm công.")
        return

    print("\n--- BẢNG CHẤM CÔNG ---")
    print(f"{'Mã NV':<10}{'Tên Nhân Viên':<25}{'Giờ Vào':<20}{'Giờ Ra'}")
    print("-" * 70)

    for r in book:
        clock_in = r['times'][0]
        clock_out = r['times'][1] if r['times'][1] else "[Đang làm việc]"

        print(
            f"{r['id']:<10}"
            f"{r['name']:<25}"
            f"{clock_in:<20}"
            f"{clock_out}"
        )