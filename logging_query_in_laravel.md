# Logging query trong Laravel

Để biết ứng dụng thực hiện câu truy vấn nào tới Database ta có thể log lại câu truy vấn đó khi nó được thực thi.

## Mục đích

Mục đich chính của việc này là ta có thể theo dõi các câu truy vấn được executed trong việc debug và tuning/optimze câu truy vấn.

## Thực hiện

Để log các query được thực thi ta chỉ cần bắt sự kiện khi ứng dụng execute query. Ta có thể hiện bằng cách truyền vào một hàm ẩn danh khi gọi đến method `listen` của class `DB`. Đoạn code cần được đặt trong method `boot` của `AppServiceProvider` hoặc của một service provide riêng tự tạo.

```php
<?php

namespace App\Providers;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        DB::listen(function ($q) {
            Log::info('TIME: ' . $q->time . '; SQL:' . $q->sql);
        });
    }

    /**
     * Register any application services.
     *
     * @return void
     */
    public function register(){}
}
```

Ở trong hàm log mình chỉ log lại __thời gian__ và __cấu trúc__ của câu truy vấn. Bạn cũng có thể log lại dữ liệu được bind vào truy vấn:

```php
Log::info('TIME: ' . $q->time . '; SQL:' . $q->sql . '; BINDINGS: ' . $q->bindings);
```

## Tham khảo

[https://laravel.com/docs/5.5/database](https://laravel.com/docs/5.5/database)
