# Cách sử dụng nhiều ssh key cho nhiều tài khoản với git

Nhiều lập trình viên dùng nhiều tài khoản git với những email khác nhau như email cá nhân và công ty thì việc xác thực sử dụng _https_ trên command line khiến mỗi lần phải gõ email và password là một nỗi khiếp sợ.

Một cách giải quyết ta có thể sử dụng là sử dụng các ứng dụng quản lý mã nguồn như GitKraken, SourceTree... để thực hiện các thao tác commit, pull, push, rebase, diff...

Tuy nhiên đối với những thao tác commit, pull, push, rebase... đơn giản như vậy thì bản thân mình cảm thấy không cần thiết tới những ứng dụng trên. Chỉ cần command line là đủ - nhẹ nhàng, nhanh chóng, chạy bất cứ đâu.

Vậy nên trong bài viết này mình sẽ giải thích làm thế nào để khiến Git chọn đúng SSH key cho project bạn đang làm việc, bất kể remote repository ở Github, Gitlab hay Bitbucket.

## Bước 1: Tạo SSH key cho tài khoản mới

Chuyển tới thư mục chứa khóa SSH:

```
cd ~/.ssh
```

Để tạo khóa mới đơn giản ta chỉ cần chạy lệnh

```
ssh-keygen -t rsa -C "tranghv" -f "tranghv"
```

Ở đây __tranghv__ có thể là bất cứ thứ gì: username của email, username của tài khoản công ty, tổ chức, cũng có thể đặt là github/bitbucket. Ở đây mình khuyến nghị đặt theo tên của username của email/tên công ty vì ta có thể dùng nó cho cả github/bitbucket. Ở đây mình chọn theo username của email mình mới có.

Tùy chọn `-C` là comment giúp xác định key. Tùy chọn `-f` chỉ ra tên của file, nó phải là duy nhất.

Nhập passpharse vào command line khi được hỏi nếu bạn muốn (recommended).

## Bước 2: Chỉnh ssh config file

Trong thư mục `~/.ssh` tạo file `config` nếu bạn chưa có:

```
touch config
```

Sửa file config thành như sau:

```
# ssh key for tranghv
    Host tranghv
    HostName bitbucket.org
    User git
    IdentityFile ~/.ssh/tranghv
```

Ở đây:

- `Host` thì ta có thể đặt tên bất kì.
- `Hostname` là địa chỉ của dịch vị bạn sử dụng.
- `User` bắt buộc là git
- `IdentityFile` là địa chỉ private key file ở bước 1

## Bước 3: Thêm priate key vào keyring

Hữu dụng nếu bạn dùng passphrase để bảo vệ private key. Nếu bạn không dùng passphrase thì bỏ qua.

```
ssh-add -K ~/.ssh/tranghv
```

## Bước 4: Cấu hình cho local Git repo

Để giúp git chọn đúng key để dùng thì bạn phải nói cho git biết.

```
git remote set-url origin git@tranghv:ower/repo-name.git
```

`tranghv` là `Host` bạn đặt ở bước 2.

## Bước 5: Thêm public key vào tài khoản remote

Bước cuối dùng ta chỉ cần copy public key và thêm vào remote account

```
cat ~/.ssh/tranghv.pub
```
Đi đến `https://bitbucket.org/account/user/<your-username>/ssh-keys/` và thêm public key.

And the, Enjoy!
