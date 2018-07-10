//
//  File.swift
//  TicTacToeChess
//
//  Created by Salman Sharif on 2018-03-25.
//  Copyright © 2018 Salman Sharif. All rights reserved.
//

import Foundation
class Piece {
    var player : String
    var x : Int
    var y : Int
    init(player : String) {
        self.player = player
        self.x = -1
        self.y = -1
    }
    
    func val_spot(x: Int, y: Int) -> Bool {
        if x >= 0 && x < 4 && y >= 0 && y < 4 {
            return true
        }else{
            return false
        }
    }
    func move(x:Int, y:Int, val_moves:[[Int]]) -> Bool {
        if <#condition#> {
            <#code#>
        }
    }
}


class Gameboard {
    let min_turn:Int = 2*2-1;
    
    var board = [[nil,nil,nil,nil],
                 [nil,nil,nil,nil],
                 [nil,nil,nil,nil],
                 [nil,nil,nil,nil]]
    var turn:Int = 0
    var curr_player : String = "1"
    
}
