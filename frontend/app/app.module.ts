// Angular Modules
import { NgModule }             from '@angular/core';
import { BrowserModule }        from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule }          from '@angular/forms';
import { HttpModule }           from '@angular/http';

// App Components
import { AppComponent }   from './app.component';
import { HomeComponent }  from './home/home';
import { LoginComponent } from './login/login';

// App Services
import { UsersService }   from './services/users.service';

// App Routes
const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent }
];

@NgModule({
  imports: [ 
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
    HttpModule
  ],
  declarations: [ 
    AppComponent,
    HomeComponent,
    LoginComponent
  ],
  providers: [
    UsersService
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule {}