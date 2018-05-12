<div>
    <p><strong>1. Tiếp cận theo column</strong></p>

    <p>Nó có lẽ là một trong những cách đơn giản nhất. Khi cần thêm một ngôn ngữ mới thì những column nào cần dịch thì mình sẽ&nbsp;thêm nó vào table. Ví dụ dưới đây là có 3 ngôn ngữ cho hai column</p>

    <p>&nbsp;</p>

    <pre><code class="language-php hljs ">
        Schema::create('posts', function (Blueprint $table) {
            $table->increments('id');
            
            $table->string('title_vi');
            $table->string('title_en');
            $table->string('title_ja');

            $table->text('content_vi');
            $table->text('content_en');
            $table->text('content_ja');
            $table->timestamps();
        });
    </code></pre>

    <p>&nbsp;</p>

    <p><strong><em>Ưu điểm:</em></strong></p>

    <p><em>Đơn giản</em>: dễ thực hiện</p>

    <p><em>Dễ truy vấn</em>: bạn không phải&nbsp;JOIN</p>

    <p><em>Dữ liệu không bị lặp</em></p>

    <p><strong><em>Nhược điểm:</em></strong></p>

    <p><em>Khó cải thiện: </em>nó chỉ làm việc tốt với 2 hoặc 3 ngôn ngữ, khi có nhiều ngôn ngữ thì nó&nbsp;không ổn</p>

    <p><em>Khó để thêm một ngôn ngữ mới</em>: Khi bạn cần thêm một ngôn ngữ mới, bạn cần phải thêm tất cả các column cần dịch vào bảng</p>

    <p><em>Dư thừa các column</em>: Khi các ngôn ngữ không phải bắt buộc, sẽ có trường hợp các cột mình không lưu gì mà để trống</p>

    <p><em>Cần xác định trước ngôn ngữ cần dịch</em>: Bạn cần phải xác định trước bạn cần dịch những ngôn ngữ nào để thêm column cho phù hợp.</p>

    <p>&nbsp;</p>

    <p><strong>2. Tiếp cận theo row</strong></p>

    <p>Cũng gần giống như hướng tiếp cận theo column, nhưng ở đây là dữ liệu lặp lại ở trong các row. Xem cí dụ bên dưới, khi đó mỗi khi có một ngôn ngữ mới thì trong bảng posts có hai &nbsp;column title và content lại được lặp lại tương ứng với ngôn ngữ trong bảng languages có id của nó.</p>

    <p>&nbsp;</p>

    <pre><code class="language-php hljs ">
        Schema::create('posts', function (Blueprint $table) {
            $table->increments('id');
            $table->integer('language')->comment("ví dụ: en - tiếng anh, vi -tiếng việt, ja - tiếng nhật");
            $table->string('title');
            $table->text('content');
            $table->timestamps();
        });
    </code></pre>

<p>&nbsp;</p>

<p><strong>Ưu điểm:</strong></p>

<p><em>Đơn giản</em>: dễ thực hiện</p>

<p><em>Dễ truy vấn</em>: Không cần JOIN</p>

<p><strong>Nhược điểm:</strong></p>

<p><em>Khó cải thiện: &nbsp;</em>giả sử có một cloumn không cần dịch cần thay đổi, thì bạn sẽ cần phải thay đổi tất cả các ngôn ngữ</p>

<p><em>Khó để thêm một ngôn ngữ mới</em>: bạn cần phải lặp lại nhiều lần khi thêm một ngôn ngữ mới</p>

<p><em>Dư thừa dữ liệu</em>: trong trường hợp các một số columns không bắt buộc thì các trường đấy bị trống</p>

<p>&nbsp;</p>

<p><strong>3. Tiếp cận theo một bảng dịch</strong></p>

<p>Giải pháp này là một trong những cách&nbsp;rõ ràng nhất về cấu trúc cơ sở dữ liệu. Tất cả những nội dung cần dịch trong một bảng, Nó phù hợp với những web động mà có&nbsp;số lượng ngôn ngữ lớn hoặc có số lượng ngôn ngữ cố định và trong tương lại sẽ thêm ngôn ngữ mới. Hãy xem ví dụ dưới đây</p>

<pre><code class="language-php hljs ">
    // bảng ngôn ngữ
    Schema::create('languages', function (Blueprint $table) {
        $table->increments('id');
        $table->string('name');
    });
    // bảng post
    Schema::create('posts', function (Blueprint $table) {
        $table->increments('id');
        $table->integer('title');
        $table->integer('content');
        $table->timestamps();
    });
    // bảng dich những column từ bảng post
    Schema::create('post_translations', function (Blueprint $table) {
        $table->increments('id');
        $table->integer('post_id');
        $table->integer('language_id');
        $table->string('title');
        $table->text('content');
        $table->timestamps();
        //@TODO: missing foreign key.
    });
</code></pre>

<p>&nbsp;</p>

<p>Ở đây column title và content trong bảng posts sẽ tương ứng với column translation_id trong bảng post_translations.</p>

<p><strong>Ưu điểm:</strong></p>

<p><em>Rõ ràng</em>:&nbsp;có quan hệ với nhau</p>

<p><em>Dễ dàng thêm ngôn ngữ mới</em>: không cần bạn phải thêm column vào bảng</p>

<p><em>Tất cả ngôn ngữ ở một bảng</em>: dễ dàng cho việc đọc và sửa dữ liệu</p>

<p><strong>Nhược điểm:</strong></p>

<p><em>Truy vấn phức tạp</em>: bạn cần phải join để lấy được ngôn ngữ</p>

<p><em>Khó sửa chữa</em>: bạn cần phải truy vấn tất cả các bảng để thgao tác thêm sửa xóa</p>

<p><em>Tất cả ngôn ngữ nằm ở một bảng</em>: nếu bảng bị lỗi thì dẫn đến tất cả dữ liệu đều bị lỗi</p>

<p>&nbsp;</p>

<p><strong>4. Tiếp cận theo hướng bổ sung thêm bảng dịch</strong></p>

<p>Hãy xem ví dụ dưới đây</p>

<p>&nbsp;</p>

<pre><code class="language-php hljs ">
    // bảng ngôn ngữ
    Schema::create('languages', function (Blueprint $table) {
        $table->increments('id');
        $table->string('name');
        $table->timestamps();
    });
    // bảng post
    Schema::create('posts', function (Blueprint $table) {
        $table->increments('id');
        $table->timestamps();
    });
    // bảng dich những column từ bảng post
    Schema::create('post_translations', function (Blueprint $table) {
        $table->increments('id');
        $table->integer('language_id');
        $table->integer('post_id');
        $table->string('title');
        $table->text('content');
        $table->timestamps();
    });
</code></pre>

<p>&nbsp;</p>

<p>Ở trong bảng <em>posts</em>, những columns nào không cần dịch thì mình vẫn dữ nguyên ở bảng đấy, còn những column nào cần dịch thì mình sẽ chuyển nó sang bảng <em>post_translations , </em>như ở ví dụ này column title và content là cần dịch nên sẽ chuyển sang bảng <em>post_translations.</em></p>

<p><strong>Ưu điểm:</strong></p>

<p><em>Rõ ràng</em>:&nbsp;có quan hệ với nhau</p>

<p><em>Dễ dàng thêm ngôn ngữ mới</em>: không cần bạn phải thêm column vào bảng</p>

<p><em>Các column dữ nguyên tên</em>: không cần phải thêm hầu tố "_lang" vào sau column</p>

<p><em>Truy vấn dễ</em>: đơn giản,&nbsp;bạn chỉ cần join là xong.</p>

<p><strong>Nhược điểm:</strong></p>

<p><em>Số lượng bảng tăng lên:&nbsp;</em>Nếu bạn tạo các bảng đa ngôn ngữ cho tất cả các bảng thì số lượng bảng sẽ tăng lên</p>

<p><strong>Kết luận:&nbsp;</strong>Trên đây là 4 cách tiếp cận để thiết kế cơ sở dữ liệu đa ngôn ngữ phổ biến, bạn hoàn toàn có thể chỉnh sửa chúng sao cho phù hợp với hệ thống của mình. Và hãy nhớ rằng, bạn chọn cách nào cho dự án của mình tùy thuộc vào dự án của bạn thế nào. Các bạn có thể tham khảo trên google rất nhiều.</p>

<p>Tham khảo: https://giaphiep.com/blog/thiet-ke-co-so-du-lieu-da-ngon-ngu-1477717502.html</p>

</div>
