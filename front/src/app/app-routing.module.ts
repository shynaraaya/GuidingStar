import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HeaderComponent} from './components/header/header.component';
import {HotelListComponent} from './components/hotel-list/hotel-list.component';
import {FlightListComponent} from './components/flight-list/flight-list.component';
import { MainComponent } from './components/main/main.component';

const routes: Routes = [
  {
    path: '/',
    component: MainComponent
  },
  {
    path: 'hotels',
    component: HotelListComponent
  },
  {
    path: 'flights',
    component: FlightListComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
