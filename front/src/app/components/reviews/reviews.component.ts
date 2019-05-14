import {Component, Input, OnInit} from '@angular/core';
import {Hotel, Review} from '../../shared/modules/models';

@Component({
  selector: 'app-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.css']
})
export class ReviewsComponent implements OnInit {
  @Input()
  review: Review;
  constructor() { }

  ngOnInit() {
  }

}
