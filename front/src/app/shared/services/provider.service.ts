import { Injectable } from '@angular/core';
import {Hotel, Flight, Review, IAuthResponse} from '../modules/models';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
<<<<<<< HEAD
import * as moment from 'moment'
=======
import { promise } from 'protractor';
>>>>>>> 8e2fc6d35b92d0d72f425865667caba6c689858c

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{
<<<<<<< HEAD
public username: string;
public logged = false;
public isAdmin = false;
public password: string;
=======
  public username: string;
  public logged = false;
>>>>>>> 8e2fc6d35b92d0d72f425865667caba6c689858c

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
<<<<<<< HEAD

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
=======
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
>>>>>>> 8e2fc6d35b92d0d72f425865667caba6c689858c
