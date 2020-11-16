### 조회 & 조건

* SELECT(데이터 조회)
```sql
SELECT * FROM 테이블명; --애스터리스크(*)는 모든 열을 의미한다.
SELECT 열명1, 열명2 FROM 테이블명; --테이블의 열명1 열명2에 대한 행을 조회
```

* WHERE(검색 조건 지정 & 조건 조합 & 패턴 매칭에 의한 검색)
```sql
SELECT 열1, 열2 FROM 테이블명 WHERE 조건식;
```
  -조건 지정
```sql
SELECT * FROM 테이블명 WHERE no = 2; 
--no열의 값이 2인 경우만 조회

SELECT * FROM 테이블명 WHERE no <> 2; 
--no열의 값이 2가 아닌 경우만 조회

SELECT * FROM 테이블명 WHERE name='홍길동';
--name열이 홍길동인 경우만 조회
--숫자가 아닌 문자열이나 날짜에 경우 '' 싱글 쿼트롤 둘러싼다.

SELECT * FROM 테이블명 WHERE name IS NULL;
--name 열이 NULL인 경우만 조회
```

  -조건 조합
```sql
SELECT * FROM 테이블명 WHERE 조건1 AND 조건2;
SELECT * FROM 테이블명 WHERE 조건1 OR 조건2;
SELECT * FROM 테이블명 WHERE NOT 조건;

--AND는 OR에 비해 우선순위가 높다. 그러므로 괄호를 통해서 우선수위를 바꿀 수 있다.
SELECT * FROM 테이블명 WHERE (a=1 OR a=2) AND (b=1 OR b=2);
```

  -패턴 매칭에 의한 검색
```sql
SELECT * FROM 테이블명 WHERE text LIKE 'SQL%';
--text라는 열에서 SQL로 시작하는 내용이 있다면 검색한다. (전방매치) 

SELECT * FROM 테이블명 WHERE text LIKE '%SQL%';
--text라는 열에서 SQL을 포함하는 내용이 있다면 검색한다. (중간매치)
--예를들어 'SQL은 RDBMS를 조작하는 언어이다'
--'LIKE는 SQL에서 사용할 수있는 술어중 하나이다'

SELECT * FROM 테이블명 WHERE text LIKE '%\%%';
--이스케이프를 통해서 % 검색하기
-- _를 검색할떄도 이스케이프 (\_) 시켜야한다.
```

### 정렬 & 연산

* ORDER BY 정렬
-ORDER BY로 오름차순 정렬하기
```sql
SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명; //기본이 오름차순
SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명 ASC;
```
-ORDER BY로 내림차순 정렬하기
```sql
SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명 DESC;
```
-복수의 열을 지정해 정렬하기
```sql
SELECT 열명 FROM 테이블명 WHERE 조건식 
ORDER BY 열명1 정렬방식, 열명2 정렬방식; //정렬방식엔 ASC나 DESC
```
* SELECT 구로 연산하기
```sql
SELECT *, price * quantity FROM 테이블명;
--price와 quantity라는 열과 그들을 곱셈한 결과를 이용해서 새로운 열를 만들어 낸다.
--열명은 price * quantity로 나온다.
```
* WHERE 구에서 연산하기
```sql
SELECT *, price * quantity AS amount FROM 테이블명 
WHERE price * quantity >= 2000;
--SELECT 구에서 지정한 별명은 WHERE 구에서 쓸 수 없다.
--처리 순서가 WHERE구 -> SELECT 구 순서이기 떄문.
```
* ORDER BY 구에서 연산하기
```sql
SELECT *, price * quantity AS amount FROM 테이블명 
WHERE price * quantity >= 2000
ORDER BY amount DESC;
--SELECT 구에서 지정한 별명을 ORDER BY 절에서는 쓸 수 있다.
--처리 순서가 WHERE 구 -> SELECT 구 -> ORDER BY 구 순서이기 때문
```
* 열의 별명 (에일리어스 alias)
```sql
SELECT *, price * quantity AS amount FROM 테이블명;
--price * quantity의 결과가 amount라는 새로운 별명으로 표시된다.
SELECT *, price * quantity amount FROM 테이블명;
--AS 키워드 생략가능
```
* 
