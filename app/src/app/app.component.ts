import { Component, ViewChild, ElementRef } from '@angular/core';
import { Sizes } from './languages_moc';
import { Item } from './item';
import { LanguageService } from './languageService';
import { Observable } from 'rxjs';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  @ViewChild('inputBox') input: ElementRef;

  title = 'Autocomplete App.';
  // You must change the Author here.
  author = 'Camilo A. Monreal';
  // You must change your email here too.
  mail = 'kmilouh@gmail.com';
  messages: Observable<string[]>;
  message = '';


  language_radioSelected: string;
  size_radioSelected: string;
  language_itemsList: Item[] = []; // Languages;
  size_itemList: Item[] = Sizes;

  modelsLanguages: Item[] = [];

  constructor(private languageService: LanguageService, private modalService: NgbModal) {
    this.language_radioSelected = '1';
    this.size_radioSelected = '5';
    languageService.getModels().subscribe(x => {
      const array = x as Item[];
      this.modelsLanguages = [];
      for (let index = 0; index < array.length; index++) {
        const element = array[index];
        this.modelsLanguages.push({ name: element.value, value: index.toString() });
      }
      this.language_itemsList = this.modelsLanguages;
    });
  }

  setFocus() {
    this.input.nativeElement.focus();
  }

  searchClient(stringcad: string) {
    if (stringcad.trim().length === 0) {
      this.messages = null;
      return;

    } else {
      stringcad = stringcad.trim();

      const wordsArray = stringcad.split(/;|,| /).filter((element, index, array) => {
        return (element.trim().length > 0);
      });
      console.log(wordsArray);
      const result = this.languageService.getLanguageList(Number.parseInt(this.language_radioSelected, 10),
        Number.parseInt(this.size_radioSelected, 10), wordsArray);

      result.subscribe(x => {
        const b: any = x;
        this.messages = b.words;
      });
    }
  }
  onselectClient(client) {
    const wordsArray = this.message.split(/;|,| /);
    const word = wordsArray[wordsArray.length - 1];
    const index = this.message.lastIndexOf(word);

    if (index > 0) {
      this.message = this.message.substring(0, index) + client;
      this.messages = null;
    }
    if (wordsArray.length == 1) {
      this.message = this.message + ' ' + client;
      this.messages = null;
    }
    this.setFocus();
  }

  open(content) {

    this.modalService.open(content, { size: 'lg' }).result.then((result) => {
    }, (reason) => {
    });
  }
}
