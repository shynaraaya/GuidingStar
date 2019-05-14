import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HeaderComponent} from './components/header/header.component';
import {HotelListComponent} from './components/hotel-list/hotel-list.component';
import {FlightListComponent} from './components/flight-list/flight-list.component';
import { MainComponent } from './components/main/main.component';
import {ReviewListComponent} from './components/review-list/review-list.component';
import {SearchCompComponent} from './components/search-comp/search-comp.component';
import { LoginComponent } from './components/login/login.component';


const routes: Routes = [
  {
    path: 'search',
    component: SearchCompComponent
  },
  {
    path: 'hotels',
    component: HotelListComponent
  },
  {
    path: 'flights',
    component: FlightListComponent
  },
  {
    path: 'reviews',
    component: ReviewListComponent
  },
  {
    path: 'login',
    component: LoginComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
