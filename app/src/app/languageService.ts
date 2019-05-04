import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { encode } from 'punycode';

@Injectable()
export class LanguageService {
    constructor(private http: HttpClient) {
    }

    getLanguageList(language: number, size: number, words: string[]) {
        const headers = new HttpHeaders();
        headers.set('Content-Type', 'application/json');
        const word = (words.join('$'));
        return this.http.get(`/complete/${language}/${size}/${word}`, { headers });
    }

    getModels() {
        const headers = new HttpHeaders();
        headers.set('Content-Type', 'application/json');
        return this.http.get(`/models`, { headers });
    }
}