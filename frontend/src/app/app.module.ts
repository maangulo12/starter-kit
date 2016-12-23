import { NgModule }             from '@angular/core';
import { BrowserModule }        from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent }   from './app.component';
import { HomeComponent } from '../pages/home/home';
import { LoginComponent } from '../pages/login/login';

const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent }
];

@NgModule({
  imports: [ 
    BrowserModule,
    RouterModule.forRoot(appRoutes)
  ],
  declarations: [ 
    AppComponent,
    HomeComponent,
    LoginComponent
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule {}