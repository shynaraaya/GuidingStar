import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { HotelListComponent } from './components/hotel-list/hotel-list.component';
import { HotelComponent } from './components/hotel/hotel.component';
import { FlightComponent } from './components/flight/flight.component';
import { FlightListComponent } from './components/flight-list/flight-list.component';
import { LoginComponent } from './components/login/login.component';
import { FooterComponent } from './components/footer/footer.component';
import {HttpClientModule} from '@angular/common/http';
import {MainService} from './shared/services/main.service';
import {ProviderService} from './shared/services/provider.service';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HotelListComponent,
    HotelComponent,
    FlightComponent,
    FlightListComponent,
    LoginComponent,
    FooterComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    MainService,
    ProviderService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
