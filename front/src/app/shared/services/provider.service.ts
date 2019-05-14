import { Injectable } from '@angular/core';
import {Hotel, Flight, Review, IAuthResponse} from '../modules/models';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import { promise } from 'protractor';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{
  public username: string;
  public logged = false;

  constructor(http: HttpClient) {
    super(http);
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
  auth(login: any, password: any) : Promise<IAuthResponse>{
    return this.post('http://localhost:8000/user/login/',{
      username: login,
      password: password
    });
  }

  logout() : Promise<any>{
    return this.post('http://localhost:8000/api/logout/', {

    });
  }
}
