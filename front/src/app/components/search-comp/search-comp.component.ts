import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../../shared/services/provider.service';
import {Flight, Hotel} from '../../shared/modules/models';

@Component({
  selector: 'app-search-comp',
  templateUrl: './search-comp.component.html',
  styleUrls: ['./search-comp.component.css']
})
export class SearchCompComponent implements OnInit {
  public inputText1: string;
  public inputText2: string;
  public needHotel: boolean;
  public flights: Flight[] = [];
  public hotels: Hotel[] = [];

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
  }

  search() {
    this.provider.getFlights().then(res => {
      this.flights = res.filter(item => item.sourceLocation.toLowerCase() === this.inputText1.toLowerCase()
        && item.destinationLocation.toLowerCase() === this.inputText2.toLowerCase());
      console.log(this.flights);
    });
    this.provider.getHotels().then(res => {
      this.hotels = res.filter(item => item.city.toLowerCase() === this.inputText2.toLowerCase());
      console.log(this.hotels);
    });
  }
}
