import { Component } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'app works, but this isn't what you want!';
  readonly API_URL = 'http://localhost:8000/api';

  constructor(private http: Http) {
    http.get(this.API_URL)
				.map(this.extractData)
				.toPromise().then((result) => {
					console.log(result);
				});
  }

	private extractData(res: Response) {
    let body = res.json();
    return body.data || { };
  }

}
