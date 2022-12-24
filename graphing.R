library(tidyverse)
library(ggplot2)
library(ggrepel)


setwd("PATH")
user_data <- read.csv('data.csv')


print(user_data)

ggplot(data = user_data,
       aes(sizeData, FOV))+
  geom_point(size = 3)+
  scale_x_continuous(breaks = round(seq(min(35), max(75), by = 5),1))+ # identifies tick mark rate
  scale_y_continuous(breaks = round(seq(min(20), max(65), by = 5), 1))+
  geom_text( # labels points on graph
    aes(x = sizeData, y = FOV, label=FOV),
    nudge_x = , nudge_y = 2,
    check_overlap = T
  )+
  annotate(geom = "rect", xmin = 40, xmax = Inf, ymin = 34, ymax = 55,
         fill = "palegreen", color = "black", alpha = 0.5)+ # green rectangle
  annotate(geom = "rect", xmin = 40, xmax = Inf, ymin = 55, ymax = 60,
           fill = "orange", color = "black", alpha = 0.5)+ # orange rectangle
  annotate(geom = "rect", xmin = 40, xmax = Inf, ymin = 60, ymax = Inf,
           fill = "red", color = "black", alpha = 0.5)+ # red rectangle
  labs(title = "FOV at 100 inch viewing distance", 
       x = "TV Size (in)", 
       y = "Field of View (°)")+
  theme(plot.title = element_text(hjust = 0.5))+
  annotate("text", x=58.75, y=35, label= "Optimal FOV")+
  annotate("text", x=58.75, y = 56, label= "Danger Territory")+
  annotate("text", x = 58.75, y = 61, label = "Outside of FOV range")

ggsave("plot.png")