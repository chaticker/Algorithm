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

### 추가 & 삭제 & 갱신
* INSERT(행 추가하기)
```sql
INSERT INTO 테이블명 VALUES (값1, 값2, ...);  
--테이블의 모든 열 구성에 맞게 입력  

INSERT INTO 테이블명(열1, 열2, ...) VALUES (값1, 값2, ...);  
--원하는 열에만 값을 입력  
--명시하지 않은 열에는 NULL이나 DEFAULT로 선언된 값이 들어간다.  
```
* DEFAULT 값
```sql
INSERT INTO 테이블명(열1, 열2) VALUES (2, DEFAULT);  
--명시적으로 Default 값으로 넣기      
INSERT INTO 테이블명(열1) VALUES (2);  
--암묵적으로 Default 값으로 넣기
```
* DELETE(삭제하기)
```sql
DELETE FROM 테이블명 \[WHERE 조건식\];  
--조건식이 없다면 모든 데이터가 삭제된다.  

TRUNCATE TABLE 테이블명;  
--모든 행을 지우려면 DELETE문으로 지우는 것보다 처리속도가 매우 빠르다.
```
* UPDATE(데이터 갱신하기)
```sql
UPDATE 테이블명 SET 열1 = 값1, 열2 = 값2, ... \[WHERE 조건식\];
```

### 정렬 & 연산

* ORDER BY 정렬

-ORDER BY로 오름차순 정렬하기
```sql
SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명; --기본이 오름차순
SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명 ASC;
```
-ORDER BY로 내림차순 정렬하기
```sql
SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명 DESC;
```
-복수의 열을 지정해 정렬하기
```sql
SELECT 열명 FROM 테이블명 WHERE 조건식 
ORDER BY 열명1 정렬방식, 열명2 정렬방식; --정렬방식엔 ASC나 DESC
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
* 함수
-ROUND 함수
-CONCAT 함수 (문자열 결합)
```sql
SELECT CONCAT(열명1, 열명2) FROM 테이블명;
--열명1이 10이고 열명2가 '개'라는 문자라면 10개로 출력된다.
```
-SUBSTRING 함수 (문자열 자르기)
```sql
SUBSTRING('가나다라마사', 1, 4)
--'가나다라'

SUBSTRING('가나다라마사', 5, 2)
--'마사'
```
-TRIM 함수 (여분의 스페이스 제거하기)
```sql
TRIM('가나다   ')
--'가나다'
```
-CURRENT_TIMESTAMP 함수 (시스템 날짜)
```sql
SELECT CURRENT_TIMESTMAP;
--시스템의 현재 날짜 출력

SELECT CURRENT_TIMESTAP + INTERVAL 1 DAY;
--1일 후로 계산
```

### CASE문으로 데이터 변환하기
* 검색 CASE문
```sql
CASE WHEN 조건식1 THEN 식1
     [WHEN 조건식2 THEN 식2 ...]
     [ELSE 식3]
     END
     
CASE WHEN 열명 IS NULL THEN 0 ELSE 열명 END
--CASE문으로 NULL값을 0으로 변환하기 
--(참고로 NULL값을 변환하는 경우라면 COALESCE 함수를 사용해도 된다.)
```
* 단순 CASE문
```sql
CASE 식1 
     WHEN 식2 THEN 식3
     [WHEN 식4 THEN 식5 ...]
     [ELSE 식6]
     END
     
CASE gender_code WHEN 1 THEN '남자'
                 WHEN 2 THEN '여자' 
                 ELSE '미지정 END "성별"
--gender_code에 따라 문자열인 남자 여자로 바꾸기     
```

### 집계함수 & 서브쿼리
