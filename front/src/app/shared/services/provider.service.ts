import { Injectable } from '@angular/core';
import {Hotel, Flight, Review, IAuthResponse} from '../modules/models';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import * as moment from 'moment'

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{
public username: string;
public logged = false;
public isAdmin = false;
public password: string;

  constructor(http: HttpClient) {
    super(http);
  }

  formatDateForDjango(date: Date){
    const time = moment(date).format('YYYY-MM-DDThh:mm');
    return time;
  }

  getHotels(): Promise<Hotel[]> {
    return this.get('http://localhost:8000/api/hotels/', {});
  }

  getFlights(): Promise<Flight[]> {
    return this.get('http://localhost:8000/api/flights/', {});
  }

  getReviews(): Promise<Review[]> {
    return this.get('http://localhost:8000/api/reviews/', {});
  }

  getMe(){
    return this.get('http://localhost:8000/user/me', {});
  }
  
  putReview(review: Review): Promise<any>{
    return this.put('http://localhost:8000/api/reviews/${review.id}/', {})
  }

  deleteReview(review: Review): Promise<any>{
    return this.delet('http://localhost:8000/api/reviews/${review.id}/', {})
  }

  postReview(Text: String, ratinG: number): Promise<any>{
    return this.post('http://localhost:8000/api/reviews/',{
      review: Text,
      rating: ratinG,
      author: this.username,
      submissionDate: this.formatDateForDjango(new Date())
    })
  }
    auth(login: string, password: string): Promise<IAuthResponse> {
      return this.post('http://localhost:8000/user/login/', {
        username: login,
        password
      })
    }
  };
