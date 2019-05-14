import { Component, OnInit } from '@angular/core';
import {Hotel, Review} from '../../shared/modules/models';
import {ProviderService} from '../../shared/services/provider.service';

@Component({
  selector: 'app-review-list',
  templateUrl: './review-list.component.html',
  styleUrls: ['./review-list.component.css']
})
export class ReviewListComponent implements OnInit {

  constructor(private provider: ProviderService) { }
  reviews: Review[] = [];
  ngOnInit() {
    this.provider.getReviews().then(res => {
      this.reviews = res;
      console.log(this.reviews);
    });
  }
}
