### 조회 & 조건

* SELECT(데이터 조회)
```sql
SELECT * FROM 테이블명; --애스터리스크(*)는 모든 열을 의미한다.
SELECT 열명1, 열명2 FROM 테이블명; --테이블의 열명1 열명2에 대한 행을 조회
```

* WHERE(검색 조건 지정 & 조건 조합)
```sql
SELECT 열1, 열2 FROM 테이블명 WHERE 조건식;

--조건 지정

SELECT * FROM 테이블명 WHERE no = 2; 
--no열의 값이 2인 경우만 조회

SELECT * FROM 테이블명 WHERE no <> 2; 
--no열의 값이 2가 아닌 경우만 조회

SELECT * FROM 테이블명 WHERE name='홍길동';
--name열이 홍길동인 경우만 조회
--숫자가 아닌 문자열이나 날짜에 경우 '' 싱글 쿼트롤 둘러싼다.

SELECT * FROM 테이블명 WHERE name IS NULL;
--name 열이 NULL인 경우만 조회

--조건 조합

SELECT * FROM 테이블명 WHERE 조건1 AND 조건2;
SELECT * FROM 테이블명 WHERE 조건1 OR 조건2;
SELECT * FROM 테이블명 WHERE NOT 조건;

--AND는 OR에 비해 우선순위가 높다. 그러므로 괄호를 통해서 우선수위를 바꿀 수 있다.
SELECT * FROM 테이블명 WHERE (a=1 OR a=2) AND (b=1 OR b=2);
```

* 
