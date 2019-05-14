import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../../shared/services/provider.service';
import {Hotel} from '../../shared/modules/models';

@Component({
  selector: 'app-hotel-list',
  templateUrl: './hotel-list.component.html',
  styleUrls: ['./hotel-list.component.css']
})
export class HotelListComponent implements OnInit {

  constructor(private provider: ProviderService) { }
  hotels: Hotel[] = [];
  ngOnInit() {
    this.provider.getHotels().then( res => {
      this.hotels = res;
      console.log(res);
    });
  }

}
