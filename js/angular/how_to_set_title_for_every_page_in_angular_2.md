# Set title trong Angular 2

Để set title thì ta sẽ sử dụng Title service trong `@angular/platform-browser` bằng cách Inject vào AppComponent thông qua constructor

```ts
import { Title } from '@angular/platform-browser';

export class AppComponent {
    // code...
    constructor(private title: Title){}
    // code...
}
```

Trong AppComponent ta lắng nghe sự kiện thay đổi URL khi điều hướng.

```ts
routeLinkChange(){
    this.router.events.filter((event) => event instanceof NavigationEnd)
        .subscribe((evt: NavigationEnd) => {
            const title = this.getDeepestRoutingData(this.route.snapshot).title;
            this.title.setTitle(title ? title : 'Default title');
        }
    );
}
```

Trong đó hàm getDeepestRoutingData() sẽ lấy `data` được đặt trong một routing nào đó như `app-routing.module.ts`

```ts
getDeepestRoutingData(routeSnapshot: ActivatedRouteSnapshot) {
    let data = routeSnapshot.data ? routeSnapshot.data : null;
    if (routeSnapshot.firstChild) {
      data = this.getDeepestRoutingData(routeSnapshot.firstChild) || data;
    }

    return data;
}
```

`app-routing.module.ts`

```ts
const routes: Routes = [
    { path: "", component: HomeComponent, pathMatch: "full"},
    { path: "about", component: AboutComponent, data: {title: 'About'}},
]
```
