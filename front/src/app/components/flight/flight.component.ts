import {Component, Input, OnInit} from '@angular/core';
import {Flight, Hotel} from '../../shared/modules/models';

@Component({
  selector: 'app-flight',
  templateUrl: './flight.component.html',
  styleUrls: ['./flight.component.css']
})
export class FlightComponent implements OnInit {
  @Input()
  flight: Flight;
  constructor() { }

  ngOnInit() {
  }
}
