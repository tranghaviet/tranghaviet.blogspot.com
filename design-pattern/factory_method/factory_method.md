# Factory Method

Factory Method là một mẫu khởi tạo. Đây là một trong những cách tốt nhất để tạo __một đối tượng__.

## Mục tiêu

- Định nghĩa một interface cho việc _tạo ra một đối tượng_, nhưng để các lớp con quyết định class nào sẽ được khởi tạo. Factory Pattern cho phép một class "hoãn việc khởi tạo" ở class con.
- Xác định constructor "ảo".
- Toán tử _new_ được coi là có hại.

## Vấn đề

Một framework cần chuẩn hóa mô hình kiến trúc cho một loạt các ứng dụng, nhưng cho phép các ứng dụng riêng lẻ định nghĩa các objects của riêng chúng.

## Thảo luận

Factory Method tạo các objects như là Template Method cài đặt một thuật toán. Một superclass (class cha) quy định các chuẩn và hành vi chung và giao việc khởi tạo cho subclass (class con).

Factory Method khiến việc thiết kế dễ tùy chỉnh hơn và chỉ phức tạp hơn một chút. Các design patterns khác yêu cầu nhiều class mới, trong khi đó Factory Method chỉ yêu cầu một class mới.

Mọi người thường dùng Factory Method như là cách chuẩn để tạo mới object; nhưng sẽ là không cần thiết nếu việc khởi tạo của class không bao giờ thay đổi hoặc việc khởi tạo diễn ra khi subclass dễ dàng bị override (như khi tạo một thao tác khởi tạo)
__Factory Method giống với Abstract Factory nhưng không nhấn mạnh vào "gia đình các class"__

## Implementation

1. Chúng ta sẽ tạo một interface Shape và các class cụ thể implementing Shape interface.

1. Định nghĩa class ShapeFactory cho phép tạo các class cụ thể  implement Shape interface.

1. Sử dụng.

[ảnh ở đây]

```

```
