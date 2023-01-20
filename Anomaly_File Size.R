#install package
library(mlbench)
library(caret)
library(dplyr)

#import data
df <- read.csv("(01-02112022)_Anomaly.csv")
head(df)
glimpse(df)
mean(complete.cases(df))

# datee <- strptime(df$Start.Time, "%H:%M")

#Split Data
splite_data <- train_test_split(df, 0.6)
train_data <- splite_data[[1]]
test_data <- splite_data[[2]]
nrow(train_data); nrow(test_data)


#train model
set.seed(99)
ctrl <- trainControl(method = "repeatedcv", 
                     number = 5,
                     verboseIter = TRUE) 

#grid search <- Tuning K
#grid <- data.frame(k = c(11,23))

knn_model <- train(Anomaly ~ File.Size + End.Time ,
                   data = train_data,
                   method = "knn",
                   trControl = ctrl
                   ) 
plot(knn_model)
#ggplot(df, aes(x=Date, y=File.Size, color=File.Size)) + geom_line()



# score + evaluate model
knn_pred <- predict(knn_model,
                    newdata = test_data)

error <- knn_pred - test_data$Anomaly
test_rmse <- sqrt(mean(error**2))

RMSE(knn_pred, test_data$Anomaly)

varImp(knn_model)



### Function
train_test_split <- function(data, train_size=0.8){
  set.seed(42) #lock results
  n <- nrow(data) #นะบจำนวนแถว
  id <- sample(1:n, size = n*train_size) #สุ่มตัวเลขทั้งหมดในแถว 1:n
  train_data <- data[id, ]
  test_data <- data[-id, ]
  
  return(list(train_data,test_data)) }

