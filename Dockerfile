# 빌드 단계
FROM maven:3.8.6-openjdk-17 AS builder
WORKDIR /app
# 의존성 다운로드 최적화를 위해 pom.xml 먼저 복사
COPY ./spring-demo/pom.xml .
RUN mvn dependency:go-offline
# 소스 코드 복사 및 빌드
COPY ./spring-demo .
RUN mvn -B package -DskipTests

# 실행 단계
FROM openjdk:17-jdk-slim
WORKDIR /app
# 빌드 단계에서 생성된 JAR 파일 복사
COPY --from=builder /app/target/spring-petclinic-*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]