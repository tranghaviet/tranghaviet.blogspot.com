# Abstract Factory

Abstract Factory là một mẫu khởi tạo. Abstract Factory được coi như là super-factory (factory của factory) vì nó tạo ra các factory khác. Các fatory được sinh ra từ Abstract Factory có thể tạo ra đối tượng như là Factory Method Pattern.

## Mục tiêu

- Cung cấp một interface để tạo một "họ của các đối tượng liên quan hoặc phụ thuộc" mà không cần chỉ ra các class cụ thể.
- Tạo ra các factories khác.
- Đóng gói các platform dependencies.
- Toán tử _new_ được coi là có hại.

## Vấn đề

Một ứng dụng di động (portable) cần đóng gói platform dependencies. Việc này giống như ta tạo một ứng dụng có thể chạy trên USB mà không cần cài thêm gì khi được dùng ở các máy tính khác nhau, do đó ứng dụng này cần đóng gói các dependencies của nó để có thể chạy được ở mọi nơi (portable applications).
Các "platforms" có thể bao gồm: windowing system, operating system, database,...

## Thảo luận
