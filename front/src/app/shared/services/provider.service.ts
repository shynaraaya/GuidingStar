import { Injectable } from '@angular/core';
import {Hotel,Flight} from '../modules/models';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
  }

  getHotels(): Promise<Hotel[]> {
    return this.get('http://localhost:8000/api/hotels/', {});
  }
  getFlights(): Promise<Flight[]> {
    return this.get('http://localhost:8000/api/flights/', {});
  }
}
