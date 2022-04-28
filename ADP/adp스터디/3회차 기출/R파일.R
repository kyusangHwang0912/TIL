getwd()
setwd("C:/Users/rbtkd/ADP 스터디/기출문제풀이/3회차 기출")
# caret 패키지 설치 및 불러오기
install.packages("caret",dependencies = c("Depends","Suggests"))
install.packages("gower")
install.packages("caret.dummyVars")
install.packages('ModelMetrics')
library(caret)

# 데이터 불러오기
data1 <- read.csv('data1.csv')
head(data1)
str(data1)


# full.model 과 min.model
full.model <- lm(price~., data=data1) #모든 변수 포함 모델
min.model <- lm(price~1, data=data1) # 상수항만 있는 모델

# 변수선택법 - 전진선택법
forward.model <- step(min.model, direction='forward', scope=list(lower=min.model, upper=full.model))
formula(forward.model)
length(forward.model$model)
summary(forward.model)

# 변수선택법 - 후진소거법
backward.model <- step(full.model, direction='backward')
formula(backward.model)
length(backward.model$model)
summary(backward.model)

# 변수선택법 - 단계적선택법
stepwise.model <- step(full.model, direction='both')
formula(stepwise.model)
length(names(stepwise.model$model))
summary(stepwise.model)
