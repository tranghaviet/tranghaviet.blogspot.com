> _Design Pattern_ là một kỹ thuật trong lập trình hướng đối tượng, nó khá quan trọng và mọi lập trình viên muốn giỏi đều phải biết. Được sử dụng thường xuyên trong các ngôn ngữ [OOP](http://vi.wikipedia.org/wiki/L%E1%BA%ADp_tr%C3%ACnh_h%C6%B0%E1%BB%9Bng_%C4%91%E1%BB%91i_t%C6%B0%E1%BB%A3ng). Nó sẽ cung cấp cho bạn các “mẫu thiết kế”, giải pháp để giải quyết các vấn đề chung, thường gặp trong lập trình. Các vấn đề mà bạn gặp phải có thể bạn sẽ tự nghĩ ra cách giải quyết nhưng có thể nó chưa phải là tối ưu. Design Pattern giúp bạn giải quyết vấn đề một cách tối ưu nhất, cung cấp cho bạn các giải pháp trong lập trình OOP.

# Tổng quan Design Pattern

__Design Pattern__ có 23 mẫu cơ bản (_GoF_) và hình dưới là mối quang hệ giữa chúng

23 mẫu cơ bản (_GoF_) và mối quang hệ giữa chúng

Trong Design Pattern có 3 nhóm bao gồm:

- __Creational Pattern__ (nhóm khởi tạo) gồm:
Abstract Factory, Factory Method, Singleton, Builder, Prototype. Nó sẽ giúp bạn trong việt khởi tạo đối tượng, như bạn biết để khởi tạo bạn phải sử dụng từ khóa new, nhóm Creational Pattern sẽ sử dụng một số thủ thuật để khởi tạo đối tượng mà bạn sẽ không nhìn thấy từ khóa này.
- __Structural Pattern__ (nhóm cấu trúc) gồm:
Adapter, Bridge, Composite, Decorator, Facade, Proxy và Flyweight.. Nó dùng để thiết lập, định nghĩa quan hệ giữa các đối tượng.
- __Behavioral Pattern__ (nhóm hành vi) gồm:
Interpreter, Template Method, Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy và Visitor. Nhóm này dùng trong thực hiện các hành vi của đối tượng.

Design Pattern giúp bạn tái sử dụng mã lệnh và dễ dàng mở rộng. Để chuẩn bị học Design Pattern bạn cần phải nắm chắc các khái niệm sau:

- Bốn đặc tính của OOP: Thừa kế, Đa hình, Trừu tượng, Bao đóng.
- Khái niệm interface và abstract. Cái này cực kỳ quan trọng, để hiểu và áp dụng 2 khái niệm này có thể sẽ mất một thời gian, nhưng khi bạn nắm chắc nó bạn sẽ thấy nó thực sự cần thiết.
- Bỏ tư duy theo lối cấu trúc, nâng tư duy hoàn toàn OOP.

# Tại sao sử dụng Design Pattern?

- Design pattern cung cấp giải pháp ở dạng tổng quát, giúp tăng tốc độ phát triển phần mềm bằng cách đưa ra các mô hình test, mô hình phát triển đã qua kiểm nghiệm. Thiết kế phần mềm hiệu quả đòi hỏi phải cân nhắc các vấn đề sẽ nảy sinh trong quá trình hiện thực hóa (implementation). Dùng lại các design pattern giúp tránh được các vấn đề tiềm ẩn có thể gây ra những lỗi lớn, dễ dàng nâng cấp, bảo trì về sau.
- Một lợi thế lớn để sử dụng một mẫu thiết kế là lập trình viên khác sẽ có thể dễ dàng nhận ra nó (đặc biệt là nếu bạn sử dụng quy ước đặt tên tốt).

# Khi nào nên sử dụng Design pattern?
Đó là khi bạn muốn giữ cho chương trình của mình thực sự đơn giản. Việc sử dụng các design pattern sẽ giúp chúng ta giảm được thời gian và công sức suy nghĩ ra các cách giải quyết cho những vấn đề đã có lời giải. Bạn có thể đọc qua cuốn _Head First Design Patterns_ để có cái nhìn tổng quát hơn về design pattern.
Hệ thống các mẫu design pattern chuẩn hiện có __23__ mẫu được định nghĩa trong cuốn _Design patterns Elements of Reusable Object Oriented Software_ mà khởi đầu là cuốn _Gang of Four (GoF)_. Các tác giả của cuốn sách là Erich Gamma, Richard Helm, Ralph Johnson và John Vlissides, hay còn được biết đến với các tên “Gang of Four” hay đơn giản là “GoF”. Hệ thống các mẫu này có thể nói là đủ và tối ưu cho việc giải quyết hết các vấn đề của bài toán phân tích thiết kế và xây dựng phần mềm trong thời điểm hiện tại. Hệ thống các mẫu design pattern được chia thành 3 nhóm: nhóm Creational (5 mẫu), nhóm Structural (7 mẫu) và nhóm Behavioral (11 mẫu).

1. __Nhóm Creational (Nhóm kiến tạo)__:
Những mẫu thiết kế này cung cấp một cách để tạo ra các đối tượng bằng cách ẩn logic khởi tạo thay vì khởi tạo các đối tượng trực tiếp sử dụng từ khóa __new__. Điều này cho phép linh hoạt hơn cho chương trình trong việc quyết định đối tượng cần phải được tạo ra cho một trường hợp sử dụng nhất định.

   1. __Abstract Factory__:
   Cung cấp một interface cho việc tạo lập các đối tượng (có liên hệ với nhau) mà không cần qui định lớp khi hay xác định lớp cụ thể (concrete) tạo mỗi đối tượng. Tần suất sử dụng: cao.
   1. __Builder__:
   Tách rời việc xây dựng (construction) một đối tượng phức tạp khỏi biểu diễn của nó sao cho cùng một tiến trình xây dựng có thể tạo được các biểu diễn khác nhau.Tần suất sử dụng: trung bình thấp.
   1. __Factory Method__:
   Định nghĩa Interface để sinh ra đối tượng nhưng để cho lớp con quyết định lớp nào được dùng để sinh ra đối tượng Factory method cho phép một lớp chuyển quá trình khởi tạo đối tượng cho lớp con.Tần suất sử dụng: cao.
   1.	__Prototype__:
   Qui định loại của các đối tượng cần tạo bằng cách dùng một đối tượng mẫu, tạo mới nhờ vào sao chép đối tượng mẫu này.Tần suất sử dụng: trung bình.
   1.	__Singleton__:
   Đảm bảo 1 class chỉ có 1 instance và cung cấp 1 điểm truy xuất toàn cục đến nó.Tần suất sử dụng: cao trung bình.

1. __Nhóm Structural (nhóm cấu trúc)__:
Các mẫu thiết kế này liên quan đến thành phần của lớp và đối tượng. Khái niệm về thừa kế được sử dụng tạo các interfaces và xác định cách tạo các đối tượng để có được các chức năng mới.

   1. __Adapter__:
   Do vấn đề tương thích, thay đổi interface của một lớp thành một interface khác phù hợp với yêu cầu người sử dụng lớp.Tần suất sử dụng: cao trung bình
   1.	__Bridge__:
   Tách rời ngữ nghĩa của một vấn đề khỏi việc cài đặt ; mục đích để cả hai bộ phận (ngữ nghĩa và cài đặt) có thể thay đổi độc lập nhau.Tần suất sử dụng: trung bình
   1.	__Composite__:
   Tổ chức các đối tượng theo cấu trúc phân cấp dạng cây; Tất cả các đối tượng trong cấu trúc được thao tác theo một cách thuần nhất như nhau.Tạo quan hệ thứ bậc bao gộp giữa các đối tượng. Client có thể xem đối tượng bao gộp và bị bao gộp như nhau -> khả năng tổng quát hoá trong code của client -> dễ phát triển, nâng cấp, bảo trì.Tần suất sử dụng: cao trung bình
   1.	__Decorator__:
   Gán thêm trách nhiệm cho đối tượng (mở rộng chức năng) vào lúc chạy (dynamically).Tần suất sử dụng: trung bình
   1.	__Facade__:
   Cung cấp một interface thuần nhất cho một tập hợp các interface trong một “hệ thống con” (subsystem). Nó định nghĩa 1 interface cao hơn các interface có sẵn để làm cho hệ thống con dễ sử dụng hơn.Tần suất sử dụng: cao
   1.	__Flyweight__:
   Sử dụng việc chia sẻ để thao tác hiệu quả trên một số lượng lớn đối tượng “cở nhỏ” (chẳng hạn paragraph, dòng, cột, ký tự…).Tần suất sử dụng: thấp
   1.	__Proxy__:
   Cung cấp đối tượng đại diện cho một đối tượng khác để hỗ trợ hoặc kiểm soát quá trình truy xuất đối tượng đó. Đối tượng thay thế gọi là proxy.Tần suất sử dụng: cao trung bình

1. __Nhóm Behavioral (nhóm hành vi)__:
Những mẫu thiết kế đặc biệt quan tâm đến giao tiếp giữa các đối tượng.
   1. __Chain of Responsibility__:
   Khắc phục việc ghép cặp giữa bộ gởi và bộ nhận thông điệp; Các đối tượng nhận thông điệp được kết nối thành một chuỗi và thông điệp được chuyển dọc theo chuỗi nầy đến khi gặp được đối tượng xử lý nó.Tránh việc gắn kết cứng giữa phần tử gởi request với phần tử nhận và xử lý request bằng cách cho phép hơn 1 đối tượng có có cơ hội xử lý request . Liên kết các đối tượng nhận request thành 1 dây chuyền rồi “pass” request xuyên qua từng đối tượng xử lý đến khi gặp đối tượng xử lý cụ thể.Tần suất sử dụng: trung bình thấp
   1.	__Command	Mỗi yêu cầu (thực hiện một thao tác nào đó) được bao bọc thành một đối tượng. Các yêu cầu sẽ được lưu trữ và gởi đi như các đối tượng.Đóng gói request vào trong một Object , nhờ đó có thể nthông số hoá chương trình nhận request và thực hiện các thao tác trên request: sắp xếp, log, undo…Tần suất sử dụng: cao trung bình
   1.	__Interpreter__:
   Hỗ trợ việc định nghĩa biểu diễn văn phạm và bộ thông dịch cho một ngôn ngữ.Tần suất sử dụng: thấp
   1.	__Iterator__:
   Truy xuất các phần tử của đối tượng dạng tập hợp tuần tự (list, array, …) mà không phụ thuộc vào biểu diễn bên trong của các phần tử.Tần suất sử dụng: cao
   1.	__Mediator__:
   Định nghĩa một đối tượng để bao bọc việc giao tiếp giữa một số đối tượng với nhau.Tần suất sử dụng: trung bình thấp
   1.	__Memento__:
   Hiệu chỉnh và trả lại như cũ trạng thái bên trong của đối tượng mà vẫn không vi phạm việc bao bọc dữ liệu.Tần suất sử dụng: thấp
   1.	__Observer__:
   Định nghĩa sự phụ thuộc một-nhiều giữa các đối tượng sao cho khi một đối tượng thay đổi trạng thái thì tất cả các đối tượng phụ thuộc nó cũng thay đổi theo.Tần suất sử dụng: cao
   1.	__State__:
   Cho phép một đối tượng thay đổi hành vi khi trạng thái bên trong của nó thay đổi , ta có cảm giác như class của đối tượng bị thay đổi.Tần suất sử dụng: trung bình
   1.	__Strategy__:
   Bao bọc một họ các thuật toán bằng các lớp đối tượng để thuật toán có thể thay đổi độc lập đối với chương trình sử dụng thuật toán.Cung cấp một họ giải thuật cho phép client chọn lựa linh động một giải thuật cụ thể khi sử dụng.Tần suất sử dụng: cao trung bình
   1.	__Template method__:
   Định nghĩa phần khung của một thuật toán, tức là một thuật toán tổng quát gọi đến một số phương thức chưa được cài đặt trong lớp cơ sở; việc cài đặt các phương thức được ủy nhiệm cho các lớp kế thừa.Tần suất sử dụng: trung bình
   1.	__Visitor__:
   Cho phép định nghĩa thêm phép toán mới tác động lên các phần tử của một cấu trúc đối tượng mà không cần thay đổi các lớp định nghĩa cấu trúc đó.Tần suất sử dụng: thấp

# Bạn có thể học Design pattern ở đâu:
- Cuốn sách nổi tiếng nhất và là khởi đầu của Design pattern là “Gang of Four (GoF)“
- Cuốn [Professional Java EE Design Pattern](http://pdf.th7.cn/down/files/1508/Professional%20Java%20EE%20Design%20Patterns.pdf) nói về Design pattern trong java, có cả source code minh họa trên trang [wrox.com](wrox.com)
- Trang mạng uy tín để bạn có thể học thêm ngoài 23 mẫu cơ bản là [Sourcemaking.com](http://sourcemaking.com/design_patterns) có code mẫu
- Kênh youtube có [“Derek Banas“](https://www.youtube.com/watch?v=vNHpsC5ng_E&list=PLF206E906175C7E07) (kênh này mình rất thích này, tác giả nói giọng rất hay và biểu cảm :) ),  và khá nhiều kênh khác.

# Xem thêm các bài hướng dẫn về Design Pattern:

<ol>
<li><a href="2016/10/gioi-thieu-ve-design-pattern.html">[Tut 1 - Design Pattern] Giới thiệu về Design Pattern</a></li>
<li><a href="2016/10/tut-2-design-pattern-singleton.html">[Tut 2 - Design Pattern] Singleton</a></li>
<li><a href="2016/10/tut-3-design-pattern-adapter.html">[Tut 3 - Design Pattern] Adapter</a></li>
<li><a href="2016/11/tut-4-design-pattern-proxy.html">[Tut 4 - Design Pattern] Proxy</a></li>
<li><a href="2016/11/tut-5-design-pattern-observer.html">[Tut 5 - Design Pattern] Observer</a></li>
<li><a href="2016/11/tut-6-design-pattern-factory.html">[Tut 6 - Design Pattern] Factory</a></li>
<li><a href="2016/11/tut-7-design-pattern-composite.html">[Tut 7 - Design Pattern] Composite</a></li>
<li><a href="">[Tut 8 - Design Pattern] Wrapper</a></li>
<li><a href="">[Tut 9 - Design Pattern] Prototype</a></li>
<li><a href="">[Tut 10 - Design Pattern] Null Object</a></li>
<li><a href="">[Tut 11 - Design Pattern] Object Pool</a></li>
<li><a href="">[Tut 12 - Design Pattern] Builder Pattern</a></li>
<li><a href="">[Tut 13 - Design Pattern] Bridge Pattern</a></li>
<li><a href="">[Tut 14 - Design Pattern] Filter/Criteria Pattern</a></li>
<li><a href="">[Tut 15 - Design Pattern] Decorator</a></li>
<li><a href="">[Tut 16 - Design Pattern] Facade Pattern</a></li>
<li><a href="">[Tut 17 - Design Pattern] Flyweight Pattern</a></li>
<li><a href="">[Tut 18 - Design Pattern] Command Pattern</a></li>
<li><a href="">[Tut 19 - Design Pattern] Interpreter Pattern</a></li>
<li><a href="">[Tut 20 - Design Pattern] Iterator Pattern</a></li>
<li><a href="">[Tut 21 - Design Pattern] Mediator Pattern</a></li>
<li><a href="">[Tut 22 - Design Pattern] Memento Pattern</a></li>
<li><a href="">[Tut 23 - Design Pattern] State Pattern</a></li>
<li><a href="">[Tut 24 - Design Pattern] Strategy Pattern</a></li>
<li><a href="">[Tut 25 - Design Pattern] Template Pattern</a></li>
<li><a href="">[Tut 26 - Design Pattern] Visitor Pattern</a></li>
<li><a href="">[Tut 27 - Design Pattern] MVC Pattern</a></li>
<li><a href="">[Tut 28 - Design Pattern] Business Delegate Pattern</a></li>
<li><a href="">[Tut 29 - Design Pattern] Composite Entity Pattern</a></li>
<li><a href="">[Tut 30 - Design Pattern] Data Access Object Pattern</a></li>
<li><a href="">[Tut 31 - Design Pattern] Front Controller Pattern</a></li>
<li><a href="">[Tut 32 - Design Pattern] Intercepting Filter Pattern</a></li>
<li><a href="">[Tut 33 - Design Pattern] Service Locator Pattern</a></li>
<li><a href="">[Tut 34 - Design Pattern] Transfer Object Pattern</a></li>
</ol>
