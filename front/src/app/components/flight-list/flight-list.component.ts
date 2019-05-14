import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../../shared/services/provider.service';
import {Flight} from '../../shared/modules/models';

@Component({
  selector: 'app-flight-list',
  templateUrl: './flight-list.component.html',
  styleUrls: ['./flight-list.component.css']
})
export class FlightListComponent implements OnInit {

  constructor(private provider: ProviderService) { }
  flights: Flight[] = [];
  ngOnInit() {
    this.provider.getFlights().then(res => {
      this.flights = res;
      console.log(res);
    });
  }
}
